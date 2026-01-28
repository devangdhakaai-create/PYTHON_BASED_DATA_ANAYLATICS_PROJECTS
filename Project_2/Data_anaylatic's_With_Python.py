import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from collections import Counter

# CYBERSECURITY INTRUSION DATA ANALYSIS

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "Cybersecurity_Intrusion_Data.csv")

# Load dataset with proper delimiter
df = pd.read_csv(csv_file, sep='\t')

print("="*70)
print("TASK 1: DATA EXPLORATION & OVERVIEW")
print("="*70)

print(f"\nDataset Shape: {df.shape}")
print(f"\nColumn Names & Types:")
print(df.dtypes)
print(f"\nFirst 5 Rows:")
print(df.head())
print(f"\nMissing Values:")
print(df.isnull().sum())
print(f"\nBasic Statistics:")
print(df.describe())

print("\n" + "="*70)
print("TASK 2: ATTACK DETECTION ANALYSIS")
print("="*70)

attack_counts = df['attack_detected'].value_counts()
print(f"\nAttack Distribution:")
print(f"  No Attack (0): {attack_counts[0]} sessions ({attack_counts[0]/len(df)*100:.1f}%)")
print(f"  Attack (1): {attack_counts[1]} sessions ({attack_counts[1]/len(df)*100:.1f}%)")

# Visualization: Attack Detection Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
axes[0].pie(attack_counts.values, labels=['No Attack', 'Attack'], autopct='%1.1f%%', 
            colors=['#2ecc71', '#e74c3c'], startangle=90)
axes[0].set_title('Attack Detection Distribution', fontsize=12, fontweight='bold')

# Bar chart
attack_counts.plot(kind='bar', ax=axes[1], color=['#2ecc71', '#e74c3c'])
axes[1].set_title('Count of Attack vs No Attack', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Attack Detected')
axes[1].set_ylabel('Count')
axes[1].set_xticklabels(['No Attack', 'Attack'], rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task2_attack_distribution.png'), dpi=300)
print("\n✓ Saved: task2_attack_distribution.png")

print("\n" + "="*70)
print("TASK 3: PROTOCOL TYPE ANALYSIS")
print("="*70)

protocol_dist = df['protocol_type'].value_counts()
print(f"\nProtocol Type Distribution:")
print(protocol_dist)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar plot
protocol_dist.plot(kind='bar', ax=axes[0], color="#3f9cdb")
axes[0].set_title('Protocol Type Distribution', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Protocol Type')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Attack by protocol
protocol_attack = pd.crosstab(df['protocol_type'], df['attack_detected'])
protocol_attack.plot(kind='bar', ax=axes[1], color=['#2ecc71', '#e74c3c'])
axes[1].set_title('Attack Distribution by Protocol Type', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Protocol Type')
axes[1].set_ylabel('Count')
axes[1].legend(['No Attack', 'Attack'])
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task3_protocol_analysis.png'), dpi=300)
print("✓ Saved: task3_protocol_analysis.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 4: ENCRYPTION TYPE ANALYSIS")
print("="*70)

encryption_dist = df['encryption_used'].value_counts()
print(f"\nEncryption Type Distribution:")
print(encryption_dist)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Encryption types
encryption_dist.plot(kind='barh', ax=axes[0], color='#9b59b6')
axes[0].set_title('Encryption Type Distribution', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Count')

# Attack rate by encryption
encryption_attack = df.groupby('encryption_used')['attack_detected'].agg(['sum', 'count'])
encryption_attack['attack_rate'] = (encryption_attack['sum'] / encryption_attack['count'] * 100)
encryption_attack['attack_rate'].plot(kind='bar', ax=axes[1], color='#e67e22')
axes[1].set_title('Attack Rate by Encryption Type', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Encryption Type')
axes[1].set_ylabel('Attack Rate (%)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task4_encryption_analysis.png'), dpi=300)
print("✓ Saved: task4_encryption_analysis.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 5: LOGIN ATTEMPTS & FAILED LOGINS ANALYSIS")
print("="*70)

print(f"\nLogin Attempts Statistics:")
print(f"  Mean: {df['login_attempts'].mean():.2f}")
print(f"  Median: {df['login_attempts'].median():.2f}")
print(f"  Min: {df['login_attempts'].min()}")
print(f"  Max: {df['login_attempts'].max()}")

print(f"\nFailed Logins Statistics:")
print(f"  Mean: {df['failed_logins'].mean():.2f}")
print(f"  Median: {df['failed_logins'].median():.2f}")
print(f"  Min: {df['failed_logins'].min()}")
print(f"  Max: {df['failed_logins'].max()}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Login attempts distribution
axes[0, 0].hist(df['login_attempts'], bins=15, color='#1abc9c', edgecolor='black')
axes[0, 0].set_title('Login Attempts Distribution', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('Number of Attempts')
axes[0, 0].set_ylabel('Frequency')

# Failed logins distribution
axes[0, 1].hist(df['failed_logins'], bins=15, color='#e74c3c', edgecolor='black')
axes[0, 1].set_title('Failed Logins Distribution', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('Number of Failed Logins')
axes[0, 1].set_ylabel('Frequency')

# Login attempts vs Attack
df.boxplot(column='login_attempts', by='attack_detected', ax=axes[1, 0])
axes[1, 0].set_title('Login Attempts by Attack Status', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel('Attack Detected')
axes[1, 0].set_ylabel('Login Attempts')
axes[1, 0].get_figure().suptitle('')

# Failed logins vs Attack
df.boxplot(column='failed_logins', by='attack_detected', ax=axes[1, 1])
axes[1, 1].set_title('Failed Logins by Attack Status', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel('Attack Detected')
axes[1, 1].set_ylabel('Failed Logins')
axes[1, 1].get_figure().suptitle('')

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task5_login_analysis.png'), dpi=300)
print("✓ Saved: task5_login_analysis.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 6: NETWORK & SESSION ANALYSIS")
print("="*70)

print(f"\nNetwork Packet Size Statistics:")
print(f"  Mean: {df['network_packet_size'].mean():.2f}")
print(f"  Median: {df['network_packet_size'].median():.2f}")
print(f"  Std Dev: {df['network_packet_size'].std():.2f}")

print(f"\nSession Duration Statistics:")
print(f"  Mean: {df['session_duration'].mean():.2f} seconds")
print(f"  Median: {df['session_duration'].median():.2f} seconds")
print(f"  Max: {df['session_duration'].max():.2f} seconds")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Packet size distribution
axes[0, 0].hist(df['network_packet_size'], bins=20, color='#f39c12', edgecolor='black')
axes[0, 0].set_title('Network Packet Size Distribution', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('Packet Size (bytes)')
axes[0, 0].set_ylabel('Frequency')

# Session duration distribution
axes[0, 1].hist(df['session_duration'], bins=20, color='#16a085', edgecolor='black')
axes[0, 1].set_title('Session Duration Distribution', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('Duration (seconds)')
axes[0, 1].set_ylabel('Frequency')

# Packet size vs Attack
df.boxplot(column='network_packet_size', by='attack_detected', ax=axes[1, 0])
axes[1, 0].set_title('Packet Size by Attack Status', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel('Attack Detected')
axes[1, 0].set_ylabel('Packet Size (bytes)')
axes[1, 0].get_figure().suptitle('')

# Session duration vs Attack
df.boxplot(column='session_duration', by='attack_detected', ax=axes[1, 1])
axes[1, 1].set_title('Session Duration by Attack Status', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel('Attack Detected')
axes[1, 1].set_ylabel('Duration (seconds)')
axes[1, 1].get_figure().suptitle('')

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task6_network_session_analysis.png'), dpi=300)
print("✓ Saved: task6_network_session_analysis.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 7: IP REPUTATION SCORE ANALYSIS")
print("="*70)

print(f"\nIP Reputation Score Statistics:")
print(f"  Mean: {df['ip_reputation_score'].mean():.3f}")
print(f"  Median: {df['ip_reputation_score'].median():.3f}")
print(f"  Min: {df['ip_reputation_score'].min():.3f}")
print(f"  Max: {df['ip_reputation_score'].max():.3f}")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# IP reputation distribution
axes[0].hist(df['ip_reputation_score'], bins=20, color='#c0392b', edgecolor='black')
axes[0].set_title('IP Reputation Score Distribution', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Reputation Score (0-1)')
axes[0].set_ylabel('Frequency')

# IP reputation vs Attack
df.boxplot(column='ip_reputation_score', by='attack_detected', ax=axes[1])
axes[1].set_title('IP Reputation Score by Attack Status', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Attack Detected')
axes[1].set_ylabel('Reputation Score')
axes[1].get_figure().suptitle('')

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task7_ip_reputation_analysis.png'), dpi=300)
print("✓ Saved: task7_ip_reputation_analysis.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 8: BROWSER TYPE & UNUSUAL ACCESS ANALYSIS")
print("="*70)

browser_dist = df['browser_type'].value_counts()
print(f"\nBrowser Type Distribution:")
print(browser_dist)

unusual_dist = df['unusual_time_access'].value_counts()
print(f"\nUnusual Time Access Distribution:")
print(f"  Normal: {unusual_dist[0]} sessions")
print(f"  Unusual: {unusual_dist[1]} sessions")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Browser distribution
browser_dist.plot(kind='barh', ax=axes[0, 0], color='#34495e')
axes[0, 0].set_title('Browser Type Distribution', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('Count')

# Browser vs Attack
browser_attack = pd.crosstab(df['browser_type'], df['attack_detected'])
browser_attack.plot(kind='bar', ax=axes[0, 1], color=['#2ecc71', '#e74c3c'])
axes[0, 1].set_title('Attack Distribution by Browser Type', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('Browser Type')
axes[0, 1].set_ylabel('Count')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].legend(['No Attack', 'Attack'])

# Unusual time access
unusual_dist.plot(kind='bar', ax=axes[1, 0], color=['#3498db', '#e67e22'])
axes[1, 0].set_title('Unusual Time Access Distribution', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel('Unusual Access')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_xticklabels(['Normal Time', 'Unusual Time'], rotation=0)

# Unusual access vs Attack
unusual_attack = pd.crosstab(df['unusual_time_access'], df['attack_detected'])
unusual_attack.plot(kind='bar', ax=axes[1, 1], color=['#2ecc71', '#e74c3c'])
axes[1, 1].set_title('Attack Distribution by Access Time', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel('Access Time')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_xticklabels(['Normal', 'Unusual'], rotation=0)
axes[1, 1].legend(['No Attack', 'Attack'])

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task8_browser_unusual_access.png'), dpi=300)
print("✓ Saved: task8_browser_unusual_access.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 9: CORRELATION ANALYSIS")
print("="*70)

# Select numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

print(f"\nCorrelation with Attack Detection:")
attack_correlation = correlation_matrix['attack_detected'].sort_values(ascending=False)
print(attack_correlation)

# Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, ax=ax, cbar_kws={'label': 'Correlation'})
ax.set_title('Correlation Matrix - Cybersecurity Intrusion Data', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'task9_correlation_heatmap.png'), dpi=300)
print("✓ Saved: task9_correlation_heatmap.png")

# ============================================================================
print("\n" + "="*70)
print("TASK 10: RISK FACTORS ANALYSIS")
print("="*70)

# Identify high-risk sessions
print(f"\nHigh-Risk Factors Analysis:")

high_failed_logins = df[df['failed_logins'] >= 3]
print(f"  Sessions with 3+ failed logins: {len(high_failed_logins)} ({len(high_failed_logins)/len(df)*100:.1f}%)")
print(f"    - Attack rate: {high_failed_logins['attack_detected'].mean()*100:.1f}%")

high_login_attempts = df[df['login_attempts'] >= 4]
print(f"  Sessions with 4+ login attempts: {len(high_login_attempts)} ({len(high_login_attempts)/len(df)*100:.1f}%)")
print(f"    - Attack rate: {high_login_attempts['attack_detected'].mean()*100:.1f}%")

unusual_sessions = df[df['unusual_time_access'] == 1]
print(f"  Sessions with unusual time access: {len(unusual_sessions)} ({len(unusual_sessions)/len(df)*100:.1f}%)")
print(f"    - Attack rate: {unusual_sessions['attack_detected'].mean()*100:.1f}%")

high_reputation = df[df['ip_reputation_score'] >= 0.5]
print(f"  Sessions with high IP reputation score (0.5+): {len(high_reputation)} ({len(high_reputation)/len(df)*100:.1f}%)")
print(f"    - Attack rate: {high_reputation['attack_detected'].mean()*100:.1f}%")

print("\n" + "="*70)
print("ANALYSIS COMPLETE!")
print("="*70)
print(f"\nAll visualizations saved to: {script_dir}")
print("\nGenerated Files:")
print("  - task2_attack_distribution.png")
print("  - task3_protocol_analysis.png")
print("  - task4_encryption_analysis.png")
print("  - task5_login_analysis.png")
print("  - task6_network_session_analysis.png")
print("  - task7_ip_reputation_analysis.png")
print("  - task8_browser_unusual_access.png")
print("  - task9_correlation_heatmap.png")
print("="*70)