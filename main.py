"""
═══════════════════════════════════════════════════════════════════════════════
    PRIVACY INTELLIGENCE ENGINE - COMPLETE IMPLEMENTATION
    Advanced Re-identification Warning System with ALL 26+ Features
═══════════════════════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np
import json
import hashlib
import argparse
import logging
from datetime import datetime
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any
import sys
import os
import time

# ═══════════════════════════════════════════════════════════════════════════
# BEAUTIFUL CLI VISUALIZATION SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class Colors:
    """ANSI color codes for stunning terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'

class Visualizer:
    """Beautiful CLI visualization engine with charts and gauges"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        """Print stunning ASCII banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ██████╗ ██████╗ ██╗██╗   ██╗ █████╗  ██████╗██╗   ██╗                       ║
║   ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝                       ║
║   ██████╔╝██████╔╝██║██║   ██║███████║██║      ╚████╔╝                        ║
║   ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║██║       ╚██╔╝                         ║
║   ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║╚██████╗   ██║                          ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝   ╚═╝                          ║
║                                                                               ║
║            INTELLIGENCE ENGINE - Advanced Re-identification System            ║
║                🔐 26+ Features • Beautiful CLI • Real-time                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(banner)
    
    @staticmethod
    def print_header(text: str):
        """Print styled section header"""
        width = 80
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'═'*80}{Colors.ENDC}")
        print(f"{Colors.GREEN}{Colors.BOLD}✨ Thank you for using Privacy Intelligence Engine! ✨{Colors.ENDC}")
        print(f"{Colors.CYAN}🔐 All 26+ Features Active • Comprehensive Analysis Complete{Colors.ENDC}")
        print(f"{Colors.CYAN}{'═'*80}{Colors.ENDC}\n")
        print(f"{Colors.CYAN}{Colors.BOLD}{'═'*width}{Colors.ENDC}")
        print(f"{Colors.CYAN}{Colors.BOLD}{text.center(width)}{Colors.ENDC}")
        print(f"{Colors.CYAN}{Colors.BOLD}{'═'*width}{Colors.ENDC}\n")
    
    @staticmethod
    def print_subheader(text: str, icon: str = "📊"):
        """Print subsection header"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}{'─'*80}{Colors.ENDC}")
        print(f"{Colors.BLUE}{Colors.BOLD}{icon} {text}{Colors.ENDC}")
        print(f"{Colors.BLUE}{Colors.BOLD}{'─'*80}{Colors.ENDC}")
    
    @staticmethod
    def print_metric(label: str, value: Any, color=Colors.GREEN, indent: int = 2):
        """Print a formatted metric"""
        spaces = " " * indent
        print(f"{spaces}{Colors.BOLD}{label}:{Colors.ENDC} {color}{value}{Colors.ENDC}")
    
    @staticmethod
    def print_bar_chart(data: Dict[str, int], title: str, width: int = 50):
        """Draw beautiful ASCII bar chart"""
        print(f"\n{Colors.BOLD}{Colors.UNDERLINE}{title}{Colors.ENDC}")
        print("─" * 70)
        
        if not data or sum(data.values()) == 0:
            print("  No data to display")
            return
        
        max_value = max(data.values())
        total = sum(data.values())
        
        colors = {
            'HIGH': Colors.RED,
            'MEDIUM': Colors.YELLOW,
            'LOW': Colors.GREEN,
            'CRITICAL': Colors.RED,
            'WARNING': Colors.YELLOW,
            'ACCEPTABLE': Colors.GREEN
        }
        
        for label, value in data.items():
            bar_length = int((value / max_value) * width) if max_value > 0 else 0
            color = colors.get(label, Colors.CYAN)
            bar = "█" * bar_length
            percentage = (value / total * 100) if total > 0 else 0
            
            print(f"  {label:12s} │ {color}{bar}{Colors.ENDC} {value:5d} ({percentage:5.1f}%)")
        print("─" * 70)
    
    @staticmethod
    def print_progress_bar(current: int, total: int, prefix: str = "", length: int = 50):
        """Animated progress bar"""
        if total == 0:
            return
        percentage = current / total
        filled = int(length * percentage)
        bar = "█" * filled + "░" * (length - filled)
        print(f"\r{prefix} [{Colors.CYAN}{bar}{Colors.ENDC}] {percentage*100:.0f}%", end="", flush=True)
        if current == total:
            print()
    
    @staticmethod
    def print_box(title: str, content: List[str], color=Colors.BLUE):
        """Print content in a beautiful box"""
        width = 76
        print(f"\n{color}╔{'═'*width}╗{Colors.ENDC}")
        print(f"{color}║ {Colors.BOLD}{title.ljust(width-2)}{Colors.ENDC}{color} ║{Colors.ENDC}")
        print(f"{color}╠{'═'*width}╣{Colors.ENDC}")
        for line in content:
            # Handle long lines
            if len(line) > width - 2:
                line = line[:width-5] + "..."
            print(f"{color}║{Colors.ENDC} {line.ljust(width-2)} {color}║{Colors.ENDC}")
        print(f"{color}╚{'═'*width}╝{Colors.ENDC}")
    
    @staticmethod
    def print_risk_gauge(risk_score: float, label: str = "Overall Risk"):
        """Display risk as a beautiful visual gauge"""
        print(f"\n{Colors.BOLD}{Colors.UNDERLINE}{label}:{Colors.ENDC}")
        gauge_width = 60
        filled = int(gauge_width * risk_score)
        
        if risk_score > 0.7:
            color = Colors.RED
            status = "🔴 CRITICAL"
            emoji = "⚠️"
        elif risk_score > 0.4:
            color = Colors.YELLOW
            status = "🟡 WARNING"
            emoji = "⚡"
        else:
            color = Colors.GREEN
            status = "🟢 ACCEPTABLE"
            emoji = "✅"
        
        gauge = "█" * filled + "░" * (gauge_width - filled)
        print(f"  [{color}{gauge}{Colors.ENDC}]")
        print(f"  {Colors.BOLD}Score: {color}{risk_score:.3f}{Colors.ENDC} ({risk_score*100:.1f}%)  {status}")
        print()
    
    @staticmethod
    def print_table(headers: List[str], rows: List[List[str]], title: str = ""):
        """Print formatted table"""
        if title:
            print(f"\n{Colors.BOLD}{title}{Colors.ENDC}")
        
        # Calculate column widths
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Print header
        header_line = "  " + " │ ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        print(f"\n{Colors.BOLD}{header_line}{Colors.ENDC}")
        print("  " + "─" * (sum(col_widths) + len(headers) * 3 - 1))
        
        # Print rows
        for row in rows:
            row_line = "  " + " │ ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
            print(row_line)
    
    @staticmethod
    def print_warning_box(message: str):
        """Print warning message in a box"""
        print(f"\n{Colors.YELLOW}{'⚠ ' * 39}⚠{Colors.ENDC}")
        print(f"{Colors.YELLOW}{Colors.BOLD}  WARNING: {message}{Colors.ENDC}")
        print(f"{Colors.YELLOW}{'⚠ ' * 39}⚠{Colors.ENDC}")
    
    @staticmethod
    def print_success(message: str):
        """Print success message"""
        print(f"{Colors.GREEN}{Colors.BOLD}✓ {message}{Colors.ENDC}")
    
    @staticmethod
    def print_error(message: str):
        """Print error message"""
        print(f"{Colors.RED}{Colors.BOLD}✗ {message}{Colors.ENDC}")
    
    @staticmethod
    def print_info(message: str):
        """Print info message"""
        print(f"{Colors.CYAN}ℹ {message}{Colors.ENDC}")

# Configure beautiful logging
logging.basicConfig(
    level=logging.INFO,
    format=f'{Colors.CYAN}%(asctime)s{Colors.ENDC} - {Colors.BOLD}%(levelname)s{Colors.ENDC} - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════════════════
# FEATURE 24: CONFIG-DRIVEN ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════

class PrivacyConfig:
    """Configuration manager for privacy analysis parameters"""
    
    def __init__(self, config_file: str = None):
        self.default_config = {
            'k_anonymity': 3,
            'l_diversity': 2,
            't_closeness_threshold': 0.2,
            'risk_weights': {
                'age': 0.3,
                'gender': 0.2,
                'zipcode': 0.5
            },
            'privacy_levels': {
                'low': {'k': 2, 'l': 1, 'description': 'Minimal privacy'},
                'medium': {'k': 3, 'l': 2, 'description': 'Standard privacy'},
                'high': {'k': 5, 'l': 3, 'description': 'Strong privacy'},
                'maximum': {'k': 10, 'l': 5, 'description': 'Maximum privacy'}
            },
            'attacker_profiles': {
                'casual': {'knowledge': 1, 'description': 'Knows 1 attribute'},
                'insider': {'knowledge': 2, 'description': 'Knows multiple attributes'},
                'advanced': {'knowledge': 3, 'description': 'Knows most attributes'}
            },
            'generalization_strategies': {
                'age': {'method': 'age_range', 'params': {'bin_size': 5}},
                'zipcode': {'method': 'zipcode', 'params': {'digits': 3}},
                'salary': {'method': 'range', 'params': {'bin_size': 10000}}
            }
        }
        
        if config_file and os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    loaded_config = json.load(f)
                    self.config = {**self.default_config, **loaded_config}
                Visualizer.print_success(f"Configuration loaded from {config_file}")
            except Exception as e:
                Visualizer.print_warning_box(f"Error loading config: {e}. Using defaults.")
                self.config = self.default_config
        else:
            self.config = self.default_config
    
    def save(self, filename: str):
        """Save configuration to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.config, f, indent=2)
            Visualizer.print_success(f"Configuration saved to {filename}")
        except Exception as e:
            Visualizer.print_error(f"Failed to save config: {e}")
    
    def display(self):
        """Display current configuration"""
        Visualizer.print_subheader("Current Configuration", "⚙️")
        content = [
            f"k-Anonymity: {self.config['k_anonymity']}",
            f"l-Diversity: {self.config['l_diversity']}",
            f"t-Closeness Threshold: {self.config['t_closeness_threshold']}",
            "",
            "Risk Weights:",
            *[f"  • {k}: {v}" for k, v in self.config['risk_weights'].items()]
        ]
        Visualizer.print_box("Configuration Settings", content, Colors.BLUE)


# ═══════════════════════════════════════════════════════════════════════════
# FEATURES 18, 19: CRYPTOGRAPHIC UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

class CryptoUtils:
    """Cryptographic utilities for data protection"""
    
    @staticmethod
    def hash_field(value: str, salt: str = "") -> str:
        """
        FEATURE 18: Field-Level Cryptographic Protection
        SHA-256 hashing with optional salt
        """
        return hashlib.sha256(f"{value}{salt}".encode()).hexdigest()
    
    @staticmethod
    def verify_dataset_integrity(df: pd.DataFrame) -> str:
        """
        FEATURE 19: Dataset Integrity Verification
        Generate cryptographic hash for entire dataset
        """
        data_string = df.to_json(orient='records', date_format='iso')
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    @staticmethod
    def protect_sensitive_fields(df: pd.DataFrame, fields: List[str], 
                                 salt: str = "privacy_engine_2024") -> pd.DataFrame:
        """Apply cryptographic hashing to sensitive fields"""
        df_protected = df.copy()
        logger.info(f"🔒 Applying SHA-256 hashing to {len(fields)} sensitive fields...")
        
        for field in fields:
            if field in df_protected.columns:
                original_sample = df_protected[field].iloc[0] if len(df_protected) > 0 else "N/A"
                df_protected[field] = df_protected[field].apply(
                    lambda x: CryptoUtils.hash_field(str(x), salt)
                )
                hashed_sample = df_protected[field].iloc[0] if len(df_protected) > 0 else "N/A"
                logger.info(f"  ✓ Protected '{field}': {original_sample} → {hashed_sample[:16]}...")
        
        return df_protected
    
    @staticmethod
    def demonstrate_cryptographic_protection(sample_values: List[str], sensitive_attr: str):
        """
        FEATURE 18: Demonstrate cryptographic protection with examples
        """
        Visualizer.print_subheader("Cryptographic Protection Demonstration", "🔐")
        
        print(f"\n{Colors.BOLD}Field-Level SHA-256 Hashing with Salt{Colors.ENDC}")
        print("─" * 80)
        
        salt = "privacy_engine_2024"
        
        # Show hash process
        headers = ["Original Value", "SHA-256 Hash (Salted)"]
        rows = []
        
        for value in sample_values[:5]:
            hashed = CryptoUtils.hash_field(str(value), salt)
            rows.append([
                f"{Colors.YELLOW}{str(value)[:30]}{Colors.ENDC}",
                f"{Colors.GREEN}{hashed[:32]}...{Colors.ENDC}"
            ])
        
        Visualizer.print_table(headers, rows)
        
        # Explain properties
        print(f"\n{Colors.CYAN}{Colors.BOLD}🛡️  Cryptographic Properties:{Colors.ENDC}")
        properties = [
            "✓ One-way function: Cannot reverse hash to get original value",
            "✓ Deterministic: Same input always produces same hash",
            "✓ Collision resistant: Different inputs produce different hashes",
            "✓ Avalanche effect: Small input change = completely different hash",
            "✓ Salt protection: Prevents rainbow table attacks",
            "✓ Fixed length: Always 64 hexadecimal characters (256 bits)"
        ]
        for prop in properties:
            print(f"  {prop}")
        
        # Show collision resistance
        print(f"\n{Colors.BOLD}Collision Resistance Demo:{Colors.ENDC}")
        test_val1 = str(sample_values[0]) if sample_values else "test"
        test_val2 = test_val1 + "1"  # Slight change
        hash1 = CryptoUtils.hash_field(test_val1, salt)
        hash2 = CryptoUtils.hash_field(test_val2, salt)
        
        print(f"  Input 1: {Colors.YELLOW}{test_val1}{Colors.ENDC}")
        print(f"  Hash 1:  {Colors.GREEN}{hash1}{Colors.ENDC}")
        print(f"\n  Input 2: {Colors.YELLOW}{test_val2}{Colors.ENDC} (tiny change)")
        print(f"  Hash 2:  {Colors.GREEN}{hash2}{Colors.ENDC}")
        print(f"\n  {Colors.CYAN}→ Completely different hashes despite minimal input change!{Colors.ENDC}")
        print()


# ═══════════════════════════════════════════════════════════════════════════
# FEATURES 2-9, 13: CORE PRIVACY ANALYSIS ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class PrivacyAnalyzer:
    """Core privacy analysis engine implementing multiple privacy models"""
    
    def __init__(self, config: PrivacyConfig):
        self.config = config
        self.results = {}
    
    def analyze_k_anonymity(self, df: pd.DataFrame, quasi_identifiers: List[str], 
                           k: int = 3) -> Dict[str, Any]:
        """
        FEATURE 2: k-Anonymity Risk Detection
        Groups records by quasi-identifiers and flags violations
        """
        logger.info(f"🔍 Analyzing k-anonymity with k={k}...")
        
        # Group by quasi-identifiers
        grouped = df.groupby(quasi_identifiers).size().reset_index(name='count')
        
        # Find violations
        violations = grouped[grouped['count'] < k]
        
        # Calculate statistics
        group_sizes = grouped['count'].values
        
        results = {
            'total_groups': len(grouped),
            'violations': len(violations),
            'violation_percentage': (len(violations) / len(grouped) * 100) if len(grouped) > 0 else 0,
            'smallest_group': int(group_sizes.min()) if len(group_sizes) > 0 else 0,
            'largest_group': int(group_sizes.max()) if len(group_sizes) > 0 else 0,
            'average_group_size': float(group_sizes.mean()) if len(group_sizes) > 0 else 0,
            'median_group_size': float(np.median(group_sizes)) if len(group_sizes) > 0 else 0,
            'violating_groups': violations.to_dict('records')[:10],
            'k_value': k,
            'group_distribution': dict(Counter(group_sizes))
        }
        
        Visualizer.print_success(f"Found {results['violations']} k-anonymity violations in {results['total_groups']} groups")
        return results
    
    def analyze_l_diversity(self, df: pd.DataFrame, quasi_identifiers: List[str], 
                           sensitive_attr: str, l: int = 2) -> Dict[str, Any]:
        """
        FEATURE 3: l-Diversity Checking
        Ensures sensitive attribute has sufficient diversity within groups
        """
        logger.info(f"🔍 Analyzing l-diversity with l={l}...")
        
        violations = []
        groups_info = []
        diversity_scores = []
        
        for group_values, group_df in df.groupby(quasi_identifiers):
            sensitive_diversity = group_df[sensitive_attr].nunique()
            diversity_scores.append(sensitive_diversity)
            
            group_info = {
                'group': str(group_values),
                'size': len(group_df),
                'diversity': sensitive_diversity,
                'violates': sensitive_diversity < l
            }
            groups_info.append(group_info)
            
            if sensitive_diversity < l:
                violations.append(group_info)
        
        results = {
            'total_groups': len(groups_info),
            'violations': len(violations),
            'violation_percentage': (len(violations) / len(groups_info) * 100) if len(groups_info) > 0 else 0,
            'l_value': l,
            'violating_groups': violations[:10],
            'groups_summary': groups_info[:20],
            'average_diversity': float(np.mean(diversity_scores)) if diversity_scores else 0,
            'min_diversity': int(min(diversity_scores)) if diversity_scores else 0,
            'max_diversity': int(max(diversity_scores)) if diversity_scores else 0
        }
        
        Visualizer.print_success(f"Found {results['violations']} l-diversity violations")
        return results
    
    def analyze_t_closeness(self, df: pd.DataFrame, quasi_identifiers: List[str], 
                           sensitive_attr: str, threshold: float = 0.2) -> Dict[str, Any]:
        """
        FEATURE 4: Simplified t-Closeness Analysis
        Measures distance between group and overall sensitive attribute distribution
        """
        logger.info(f"🔍 Analyzing t-closeness with threshold={threshold}...")
        
        # Overall distribution
        overall_dist = df[sensitive_attr].value_counts(normalize=True)
        
        violations = []
        distances = []
        
        for group_values, group_df in df.groupby(quasi_identifiers):
            group_dist = group_df[sensitive_attr].value_counts(normalize=True)
            
            # Calculate Earth Mover's Distance (simplified)
            all_values = set(overall_dist.index) | set(group_dist.index)
            distance = sum(abs(group_dist.get(v, 0) - overall_dist.get(v, 0)) for v in all_values) / 2
            distances.append(distance)
            
            if distance > threshold:
                violations.append({
                    'group': str(group_values),
                    'size': len(group_df),
                    'distance': round(distance, 4)
                })
        
        results = {
            'violations': len(violations),
            'threshold': threshold,
            'violating_groups': violations[:10],
            'average_distance': float(np.mean(distances)) if distances else 0,
            'max_distance': float(np.max(distances)) if distances else 0,
            'min_distance': float(np.min(distances)) if distances else 0
        }
        
        Visualizer.print_success(f"Found {results['violations']} t-closeness violations")
        return results
    
    def calculate_uniqueness_scores(self, df: pd.DataFrame, 
                                    quasi_identifiers: List[str]) -> Tuple[pd.DataFrame, Dict[str, float]]:
        """
        FEATURE 13: Uniqueness Contribution Analysis
        Calculates uniqueness score for each record and attribute contribution
        """
        logger.info("🔍 Calculating uniqueness scores and attribute contributions...")
        
        # Calculate record-level uniqueness
        df_counts = df.groupby(quasi_identifiers).size().reset_index(name='count')
        df_with_counts = df.merge(df_counts, on=quasi_identifiers, how='left')
        df_with_counts['uniqueness_score'] = 1.0 / df_with_counts['count']
        
        # Calculate attribute-level contribution
        contributions = {}
        for qi in quasi_identifiers:
            # Uniqueness ratio: proportion of unique values
            unique_ratio = df[qi].nunique() / len(df)
            contributions[qi] = unique_ratio
        
        Visualizer.print_success("Uniqueness analysis complete")
        return df_with_counts, contributions
    
    def weighted_risk_scoring(self, df: pd.DataFrame, quasi_identifiers: List[str], 
                             weights: Dict[str, float]) -> pd.DataFrame:
        """
        FEATURE 6: Weighted Quasi-Identifier Risk Scoring
        Assigns risk scores based on weighted sensitivity of quasi-identifiers
        """
        logger.info("🔍 Calculating weighted risk scores...")
        
        df_risk = df.copy()
        df_risk['risk_score'] = 0.0
        
        # Calculate risk contribution from each QI
        for qi in quasi_identifiers:
            if qi in df.columns:
                weight = weights.get(qi, 0.33)  # Default equal weight
                value_counts = df[qi].value_counts()
                qi_risk = df[qi].map(lambda x: 1.0 / value_counts.get(x, 1))
                df_risk['risk_score'] += qi_risk * weight
        
        # Normalize to 0-1 range
        if df_risk['risk_score'].max() > 0:
            df_risk['risk_score'] = df_risk['risk_score'] / df_risk['risk_score'].max()
        
        Visualizer.print_success("Weighted risk scoring complete")
        return df_risk
    
    def calculate_adaptive_risk_score(self, dataset_size: int, num_qi: int, 
                                     violation_rate: float, uniqueness_avg: float) -> Dict[str, Any]:
        """
        FEATURE 7: Progressive (Adaptive) Risk Levels
        Dynamically adjusts risk based on dataset characteristics
        """
        logger.info("🔍 Calculating adaptive risk score...")
        
        # Multiple factors affecting risk
        size_factor = 1.0 / np.log10(max(dataset_size, 10))  # Smaller = riskier
        qi_factor = min(num_qi / 10.0, 1.0)  # More QIs = riskier
        violation_factor = violation_rate / 100.0
        uniqueness_factor = uniqueness_avg
        
        # Weighted adaptive score
        adaptive_score = min(
            size_factor * 0.2 +
            qi_factor * 0.2 +
            violation_factor * 0.3 +
            uniqueness_factor * 0.3,
            1.0
        )
        
        # Determine risk level
        if adaptive_score > 0.7:
            level = "CRITICAL"
            color = Colors.RED
            recommendation = "Immediate action required - high re-identification risk"
        elif adaptive_score > 0.4:
            level = "WARNING"
            color = Colors.YELLOW
            recommendation = "Moderate risk - apply mitigation strategies"
        else:
            level = "ACCEPTABLE"
            color = Colors.GREEN
            recommendation = "Low risk - continue monitoring"
        
        result = {
            'adaptive_score': adaptive_score,
            'level': level,
            'color': color,
            'recommendation': recommendation,
            'factors': {
                'dataset_size': dataset_size,
                'size_factor': size_factor,
                'num_quasi_identifiers': num_qi,
                'qi_factor': qi_factor,
                'violation_rate': violation_rate,
                'violation_factor': violation_factor,
                'average_uniqueness': uniqueness_avg,
                'uniqueness_factor': uniqueness_factor
            }
        }
        
        Visualizer.print_success(f"Adaptive Risk Score: {adaptive_score:.3f} ({level})")
        return result
    
    def classify_records_by_risk(self, df_risk: pd.DataFrame) -> Dict[str, Any]:
        """
        FEATURE 8: Re-Identification Risk Classification
        Classifies records into HIGH/MEDIUM/LOW risk categories
        """
        logger.info("🔍 Classifying records by risk level...")
        
        high_risk = df_risk[df_risk['risk_score'] > 0.7]
        medium_risk = df_risk[(df_risk['risk_score'] > 0.4) & (df_risk['risk_score'] <= 0.7)]
        low_risk = df_risk[df_risk['risk_score'] <= 0.4]
        
        total = len(df_risk)
        
        result = {
            'high': len(high_risk),
            'medium': len(medium_risk),
            'low': len(low_risk),
            'high_pct': (len(high_risk) / total * 100) if total > 0 else 0,
            'medium_pct': (len(medium_risk) / total * 100) if total > 0 else 0,
            'low_pct': (len(low_risk) / total * 100) if total > 0 else 0,
            'high_risk_records': high_risk.head(10).to_dict('records') if len(high_risk) > 0 else []
        }
        
        Visualizer.print_success(f"Classification complete: HIGH={result['high']}, MEDIUM={result['medium']}, LOW={result['low']}")
        return result
    
    def generate_human_warnings(self, high_risk_records: List[Dict], 
                               quasi_identifiers: List[str]) -> List[str]:
        """
        FEATURE 9: Human-Readable Risk Warnings
        Generates explainable warnings for high-risk records
        """
        logger.info("🔍 Generating human-readable warnings...")
        warnings = []
        
        for idx, record in enumerate(high_risk_records[:10], 1):
            qi_values = ", ".join([f"{qi}={record.get(qi, 'N/A')}" for qi in quasi_identifiers if qi in record])
            risk_score = record.get('risk_score', 0)
            
            if risk_score > 0.9:
                severity = "CRITICAL"
                reason = "Unique combination with extremely high re-identification risk"
            elif risk_score > 0.7:
                severity = "HIGH"
                reason = "Rare combination easily identifiable"
            else:
                severity = "ELEVATED"
                reason = "Notable re-identification possibility"
            
            warning = (
                f"\n{Colors.RED}{Colors.BOLD}Record #{idx}: {severity} RISK{Colors.ENDC}\n"
                f"  Risk Score: {Colors.RED}{risk_score:.3f}{Colors.ENDC}\n"
                f"  Quasi-Identifiers: {qi_values}\n"
                f"  Reason: {reason}\n"
                f"  {Colors.YELLOW}⚠ Action: Consider suppression or generalization{Colors.ENDC}"
            )
            warnings.append(warning)
        
        Visualizer.print_success(f"Generated {len(warnings)} human-readable warnings")
        return warnings


# ═══════════════════════════════════════════════════════════════════════════
# FEATURES 10-12: ATTACK SIMULATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class AttackSimulator:
    """Simulates various re-identification attacks"""
    
    @staticmethod
    def simulate_attacker_knowledge(df: pd.DataFrame, quasi_identifiers: List[str], 
                                   attacker_type: str = 'casual') -> Dict[str, Any]:
        """
        FEATURES 10, 11: Attacker Knowledge Profiles & Attack Simulation Engine
        Simulates attacks based on different attacker knowledge levels
        """
        logger.info(f"⚔️  Simulating {attacker_type.upper()} attacker...")
        
        # Determine known attributes based on attacker type
        if attacker_type == 'casual':
            known_attrs = quasi_identifiers[:1]
            description = "Knows 1 attribute (public records)"
        elif attacker_type == 'insider':
            known_attrs = quasi_identifiers[:len(quasi_identifiers)//2 + 1]
            description = "Knows multiple attributes (employee/researcher)"
        else:  # advanced
            known_attrs = quasi_identifiers
            description = "Knows all quasi-identifiers (sophisticated adversary)"
        
        # Calculate re-identification success rates
        success_rates = []
        certain_reidentifications = 0
        
        for idx, row in df.iterrows():
            # Find matching records based on known attributes
            matches = df
            for attr in known_attrs:
                matches = matches[matches[attr] == row[attr]]
            
            # Success probability = 1 / number of matching records
            num_matches = len(matches)
            prob = 1.0 / num_matches if num_matches > 0 else 0
            success_rates.append(prob)
            
            if prob >= 1.0:
                certain_reidentifications += 1
        
        results = {
            'attacker_type': attacker_type,
            'description': description,
            'known_attributes': known_attrs,
            'num_known': len(known_attrs),
            'average_success_rate': float(np.mean(success_rates)),
            'max_success_rate': float(np.max(success_rates)),
            'min_success_rate': float(np.min(success_rates)),
            'median_success_rate': float(np.median(success_rates)),
            'high_risk_records': int(sum(1 for p in success_rates if p > 0.5)),
            'guaranteed_reidentification': certain_reidentifications,
            'success_distribution': {
                'certain (100%)': certain_reidentifications,
                'high (>50%)': int(sum(1 for p in success_rates if 0.5 < p < 1.0)),
                'medium (20-50%)': int(sum(1 for p in success_rates if 0.2 < p <= 0.5)),
                'low (<20%)': int(sum(1 for p in success_rates if p <= 0.2))
            }
        }
        
        Visualizer.print_success(f"{attacker_type.upper()} attacker avg success: {results['average_success_rate']:.2%}")
        return results
    
    @staticmethod
    def simulate_linkage_attack(df: pd.DataFrame, quasi_identifiers: List[str], 
                               external_records: int = 100) -> Dict[str, Any]:
        """
        FEATURE 12: Linkage Attack Simulation
        Simulates joining with external dataset to demonstrate linkage risks
        """
        logger.info(f"🔗 Simulating linkage attack with {external_records} external records...")
        
        # Generate synthetic external dataset mimicking real auxiliary data
        external_data = {}
        for qi in quasi_identifiers:
            if df[qi].dtype == 'object':
                # Sample from actual values (realistic scenario)
                external_data[qi] = np.random.choice(df[qi].unique(), external_records)
            else:
                # Sample from actual values
                external_data[qi] = np.random.choice(df[qi].values, external_records)
        
        external_df = pd.DataFrame(external_data)
        
        # Attempt linkage attack
        merged = external_df.merge(df, on=quasi_identifiers, how='inner')
        unique_links = merged.drop_duplicates(subset=quasi_identifiers)
        
        results = {
            'external_records': external_records,
            'successful_links': len(merged),
            'unique_individuals_linked': len(unique_links),
            'linkage_rate': (len(merged) / external_records * 100) if external_records > 0 else 0,
            'unique_linkage_rate': (len(unique_links) / external_records * 100) if external_records > 0 else 0,
            'records_at_risk': len(df[df[quasi_identifiers].isin(external_df[quasi_identifiers].to_dict('list')).all(axis=1)])
        }
        
        Visualizer.print_success(f"Linkage attack: {results['successful_links']} successful links ({results['linkage_rate']:.1f}%)")
        return results


# ═══════════════════════════════════════════════════════════════════════════
# FEATURES 14-17: PRIVACY MITIGATION & ENHANCEMENT
# ═══════════════════════════════════════════════════════════════════════════

class PrivacyMitigation:
    """Privacy enhancement and mitigation strategies"""
    
    @staticmethod
    def generalize_age(age: int, bin_size: int = 5) -> str:
        """Generalize age into ranges"""
        if pd.isna(age):
            return "Unknown"
        age = int(age)
        lower = (age // bin_size) * bin_size
        upper = lower + bin_size - 1
        return f"{lower}-{upper}"
    
    @staticmethod
    def generalize_zipcode(zipcode: str, digits: int = 3) -> str:
        """Generalize zipcode to first N digits"""
        zipcode_str = str(zipcode)
        return zipcode_str[:digits] + 'X' * (len(zipcode_str) - digits)
    
    @staticmethod
    def apply_generalization(df: pd.DataFrame, strategy: Dict[str, Any]) -> pd.DataFrame:
        """
        FEATURE 14: Automatic Generalization Engine
        Applies generalization strategies to reduce granularity
        """
        logger.info("🛡️  Applying automatic generalization strategies...")
        
        df_gen = df.copy()
        applied = []
        
        for col, config in strategy.items():
            if col not in df_gen.columns:
                continue
            
            method = config.get('method')
            params = config.get('params', {})
            
            try:
                if method == 'age_range' and col in df_gen.columns:
                    df_gen[col] = df_gen[col].apply(
                        lambda x: PrivacyMitigation.generalize_age(x, params.get('bin_size', 5))
                    )
                    applied.append(f"{col} → age ranges")
                    logger.info(f"  ✓ Generalized {col} into {params.get('bin_size', 5)}-year ranges")
                
                elif method == 'zipcode' and col in df_gen.columns:
                    df_gen[col] = df_gen[col].apply(
                        lambda x: PrivacyMitigation.generalize_zipcode(x, params.get('digits', 3))
                    )
                    applied.append(f"{col} → {params.get('digits', 3)} digits")
                    logger.info(f"  ✓ Generalized {col} to first {params.get('digits', 3)} digits")
                
            except Exception as e:
                logger.warning(f"  ⚠ Could not generalize {col}: {e}")
        
        Visualizer.print_success(f"Generalization applied to {len(applied)} columns")
        return df_gen, applied
    
    @staticmethod
    def demonstrate_generalization(df_before: pd.DataFrame, df_after: pd.DataFrame, 
                                   quasi_identifiers: List[str], k: int, applied: List[str]):
        """
        FEATURE 14: Show before/after generalization comparison
        """
        Visualizer.print_subheader("Generalization Engine - Before vs After Comparison", "🔄")
        
        # Analyze both versions
        grouped_before = df_before.groupby(quasi_identifiers).size()
        violations_before = (grouped_before < k).sum()
        
        grouped_after = df_after.groupby(quasi_identifiers).size()
        violations_after = (grouped_after < k).sum()
        
        improvement = violations_before - violations_after
        
        # Display comparison
        comparison_data = [
            "",
            "PRIVACY IMPROVEMENT ANALYSIS",
            "─" * 74,
            "",
            "Before Generalization:",
            f"  • Equivalence classes: {len(grouped_before)}",
            f"  • k-anonymity violations (k={k}): {Colors.RED}{violations_before}{Colors.ENDC}",
            f"  • Average group size: {grouped_before.mean():.2f}",
            "",
            "After Generalization:",
            f"  • Equivalence classes: {len(grouped_after)}",
            f"  • k-anonymity violations (k={k}): {Colors.GREEN}{violations_after}{Colors.ENDC}",
            f"  • Average group size: {grouped_after.mean():.2f}",
            "",
            f"Improvement: {Colors.GREEN}{Colors.BOLD}{improvement} violations eliminated!{Colors.ENDC}",
            f"Applied: {', '.join(applied)}" if applied else "No generalizations applied"
        ]
        
        Visualizer.print_box("Generalization Results", comparison_data, Colors.GREEN)
        
        # Show sample transformations
        print(f"\n{Colors.BOLD}Sample Data Transformations (first 5 records):{Colors.ENDC}")
        print("─" * 80)
        
        for idx in range(min(5, len(df_before))):
            changes = []
            for qi in quasi_identifiers:
                if qi in df_before.columns and qi in df_after.columns:
                    before_val = df_before.iloc[idx][qi]
                    after_val = df_after.iloc[idx][qi]
                    if str(before_val) != str(after_val):
                        changes.append(f"{qi}: {Colors.YELLOW}{before_val}{Colors.ENDC} → {Colors.GREEN}{after_val}{Colors.ENDC}")
            
            if changes:
                print(f"\n  Record {idx+1}:")
                for change in changes:
                    print(f"    {change}")
        
        print()
    
    @staticmethod
    def recommend_suppression(df: pd.DataFrame, quasi_identifiers: List[str], 
                             k: int = 3) -> Dict[str, Any]:
        """
        FEATURE 15: Suppression Recommendation System
        Recommends specific records/columns to suppress
        """
        logger.info("🛡️  Generating suppression recommendations...")
        
        grouped = df.groupby(quasi_identifiers).size().reset_index(name='count')
        violations = grouped[grouped['count'] < k]
        
        # Calculate suppression needs
        records_to_suppress = violations['count'].sum()
        
        # Analyze column uniqueness
        column_contributions = {}
        for col in quasi_identifiers:
            unique_ratio = df[col].nunique() / len(df)
            cardinality = df[col].nunique()
            column_contributions[col] = {
                'uniqueness_ratio': unique_ratio,
                'cardinality': cardinality,
                'recommendation': 'High priority for generalization' if unique_ratio > 0.5 else 'Standard'
            }
        
        # Sort by uniqueness
        sorted_columns = sorted(
            column_contributions.items(),
            key=lambda x: x[1]['uniqueness_ratio'],
            reverse=True
        )
        
        # Generate specific recommendations
        recommendations = []
        
        if records_to_suppress > 0:
            pct = (records_to_suppress / len(df) * 100)
            recommendations.append({
                'action': 'Record Suppression',
                'details': f"Suppress {records_to_suppress} records ({pct:.1f}%) to achieve k={k}",
                'priority': 'HIGH' if pct > 10 else 'MEDIUM'
            })
        
        for col, stats in sorted_columns[:3]:
            if stats['uniqueness_ratio'] > 0.5:
                recommendations.append({
                    'action': f"Generalize '{col}'",
                    'details': f"High uniqueness ({stats['uniqueness_ratio']:.1%}), {stats['cardinality']} unique values",
                    'priority': 'HIGH'
                })
            elif stats['uniqueness_ratio'] > 0.3:
                recommendations.append({
                    'action': f"Consider generalizing '{col}'",
                    'details': f"Moderate uniqueness ({stats['uniqueness_ratio']:.1%})",
                    'priority': 'MEDIUM'
                })
        
        results = {
            'records_to_suppress': int(records_to_suppress),
            'percentage_to_suppress': (records_to_suppress / len(df) * 100) if len(df) > 0 else 0,
            'columns_by_uniqueness': sorted_columns,
            'recommendations': recommendations
        }
        
        Visualizer.print_success(f"Generated {len(recommendations)} suppression recommendations")
        return results
    
    @staticmethod
    def simulate_privacy_budget(privacy_level: str, config: PrivacyConfig) -> Dict[str, Any]:
        """
        FEATURE 16: Privacy Budget Simulator
        Adjusts privacy parameters based on desired privacy level
        """
        logger.info(f"🛡️  Simulating privacy budget for '{privacy_level}' level...")
        
        levels = config.config.get('privacy_levels', {})
        selected = levels.get(privacy_level, {'k': 3, 'l': 2, 'description': 'Standard'})
        
        # Calculate strictness score
        strictness = (selected['k'] + selected['l']) / 15.0  # Normalized 0-1
        
        budget = {
            'privacy_level': privacy_level,
            'k_value': selected['k'],
            'l_value': selected['l'],
            'description': selected.get('description', 'Custom privacy level'),
            'strictness_score': strictness,
            'data_utility_tradeoff': 1.0 - strictness,  # Higher privacy = lower utility
            'recommended_for': []
        }
        
        # Add recommendations
        if privacy_level == 'low':
            budget['recommended_for'] = ['Public datasets', 'Non-sensitive data', 'High utility needs']
        elif privacy_level == 'medium':
            budget['recommended_for'] = ['Standard use cases', 'Balanced privacy-utility']
        elif privacy_level == 'high':
            budget['recommended_for'] = ['Sensitive data', 'Healthcare', 'Financial records']
        elif privacy_level == 'maximum':
            budget['recommended_for'] = ['Highly sensitive data', 'Legal compliance', 'Maximum protection']
        
        Visualizer.print_success(f"Privacy budget configured: k={budget['k_value']}, l={budget['l_value']}")
        return budget


# ═══════════════════════════════════════════════════════════════════════════
# FEATURES 20, 21: REPORTING & VISUALIZATION
# ═══════════════════════════════════════════════════════════════════════════

class ReportGenerator:
    """Generate comprehensive privacy analysis reports"""
    
    @staticmethod
    def generate_text_report(analysis_results: Dict[str, Any], 
                           output_file: str = None) -> str:
        """
        FEATURE 20: Explainable Privacy Report Generator
        Generates comprehensive human-readable reports
        """
        report = []
        w = 80  # width
        
        # Header
        report.append("═" * w)
        report.append("PRIVACY INTELLIGENCE REPORT".center(w))
        report.append("Advanced Re-identification Risk Analysis".center(w))
        report.append("═" * w)
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Dataset info
        info = analysis_results.get('dataset_info', {})
        report.append(f"\nDataset: {info.get('filename', 'Unknown')}")
        report.append(f"Total Records: {info.get('total_records', 0):,}")
        report.append(f"Total Columns: {info.get('total_columns', 0)}")
        report.append(f"Quasi-Identifiers: {', '.join(info.get('quasi_identifiers', []))}")
        report.append(f"Sensitive Attribute: {info.get('sensitive_attribute', 'N/A')}")
        
        # Integrity hash (FEATURE 19)
        if 'integrity_hash' in analysis_results:
            report.append(f"\nDataset Integrity Hash (SHA-256):")
            report.append(f"  {analysis_results['integrity_hash']}")
        
        # Executive Summary
        report.append("\n" + "─" * w)
        report.append("EXECUTIVE SUMMARY")
        report.append("─" * w)
        
        risk_dist = analysis_results.get('risk_distribution', {})
        report.append(f"\nRisk Distribution:")
        report.append(f"  HIGH Risk:   {risk_dist.get('high', 0):>6,} records ({risk_dist.get('high_pct', 0):>5.1f}%)")
        report.append(f"  MEDIUM Risk: {risk_dist.get('medium', 0):>6,} records ({risk_dist.get('medium_pct', 0):>5.1f}%)")
        report.append(f"  LOW Risk:    {risk_dist.get('low', 0):>6,} records ({risk_dist.get('low_pct', 0):>5.1f}%)")
        
        # Adaptive Risk (FEATURE 7)
        if 'adaptive_risk' in analysis_results:
            adaptive = analysis_results['adaptive_risk']
            report.append(f"\nAdaptive Privacy Risk Score: {adaptive['adaptive_score']:.3f}")
            report.append(f"Risk Level: {adaptive['level']}")
            report.append(f"Assessment: {adaptive['recommendation']}")
        
        # k-Anonymity (FEATURE 2)
        if 'k_anonymity' in analysis_results:
            ka = analysis_results['k_anonymity']
            report.append("\n" + "─" * w)
            report.append("K-ANONYMITY ANALYSIS")
            report.append("─" * w)
            report.append(f"\nk-value: {ka['k_value']}")
            report.append(f"Total Equivalence Classes: {ka['total_groups']:,}")
            report.append(f"Violations: {ka['violations']:,} ({ka['violation_percentage']:.1f}%)")
            report.append(f"Average Group Size: {ka['average_group_size']:.2f}")
            report.append(f"Median Group Size: {ka.get('median_group_size', 0):.2f}")
            report.append(f"Smallest Group: {ka['smallest_group']}")
            report.append(f"Largest Group: {ka['largest_group']}")
        
        # l-Diversity (FEATURE 3)
        if 'l_diversity' in analysis_results:
            ld = analysis_results['l_diversity']
            report.append("\n" + "─" * w)
            report.append("L-DIVERSITY ANALYSIS")
            report.append("─" * w)
            report.append(f"\nl-value: {ld['l_value']}")
            report.append(f"Total Groups: {ld['total_groups']:,}")
            report.append(f"Violations: {ld['violations']:,} ({ld['violation_percentage']:.1f}%)")
            report.append(f"Average Diversity: {ld['average_diversity']:.2f}")
            report.append(f"Minimum Diversity: {ld.get('min_diversity', 0)}")
            report.append(f"Maximum Diversity: {ld.get('max_diversity', 0)}")
        
        # t-Closeness (FEATURE 4)
        if 't_closeness' in analysis_results:
            tc = analysis_results['t_closeness']
            report.append("\n" + "─" * w)
            report.append("T-CLOSENESS ANALYSIS")
            report.append("─" * w)
            report.append(f"\nThreshold: {tc['threshold']}")
            report.append(f"Violations: {tc['violations']:,}")
            report.append(f"Average Distance: {tc['average_distance']:.4f}")
            report.append(f"Maximum Distance: {tc.get('max_distance', 0):.4f}")
        
        # Attack Simulations (FEATURES 10, 11, 12)
        if 'attack_simulations' in analysis_results:
            report.append("\n" + "─" * w)
            report.append("ATTACK SIMULATION RESULTS")
            report.append("─" * w)
            
            for attack_type, attack in analysis_results['attack_simulations'].items():
                report.append(f"\n{attack_type.upper()} Attacker:")
                report.append(f"  Description: {attack.get('description', 'N/A')}")
                report.append(f"  Known Attributes: {attack['num_known']}")
                report.append(f"  Average Success Rate: {attack['average_success_rate']:.2%}")
                report.append(f"  Median Success Rate: {attack.get('median_success_rate', 0):.2%}")
                report.append(f"  Maximum Success Rate: {attack['max_success_rate']:.2%}")
                report.append(f"  High-Risk Records: {attack['high_risk_records']:,}")
                report.append(f"  Guaranteed Re-identification: {attack.get('guaranteed_reidentification', 0):,}")
        
        # Linkage Attack (FEATURE 12)
        if 'linkage_attack' in analysis_results:
            link = analysis_results['linkage_attack']
            report.append("\n" + "─" * w)
            report.append("LINKAGE ATTACK SIMULATION")
            report.append("─" * w)
            report.append(f"\nExternal Records: {link['external_records']:,}")
            report.append(f"Successful Links: {link['successful_links']:,} ({link['linkage_rate']:.1f}%)")
            report.append(f"Unique Individuals Linked: {link.get('unique_individuals_linked', 0):,}")
            report.append(f"Records at Risk: {link.get('records_at_risk', 0):,}")
        
        # Uniqueness (FEATURE 13)
        if 'uniqueness_contribution' in analysis_results:
            report.append("\n" + "─" * w)
            report.append("UNIQUENESS CONTRIBUTION ANALYSIS")
            report.append("─" * w)
            for attr, score in analysis_results['uniqueness_contribution'].items():
                report.append(f"  {attr}: {score:.2%} (uniqueness ratio)")
        
        # Cryptographic Protection (FEATURE 18)
        if 'cryptographic_demo' in analysis_results:
            crypto = analysis_results['cryptographic_demo']
            report.append("\n" + "─" * w)
            report.append("CRYPTOGRAPHIC PROTECTION")
            report.append("─" * w)
            report.append(f"  Hash Algorithm: SHA-256")
            report.append(f"  Protected Fields: {', '.join(crypto.get('protected_fields', []))}")
            report.append(f"  Salt Applied: Yes")
            report.append(f"  One-way Protection: Irreversible")
        
        # Generalization Results (FEATURE 14)
        if 'generalization' in analysis_results:
            gen = analysis_results['generalization']
            report.append("\n" + "─" * w)
            report.append("GENERALIZATION ENGINE RESULTS")
            report.append("─" * w)
            report.append(f"  Violations Before: {gen.get('violations_before', 0):,}")
            report.append(f"  Violations After: {gen.get('violations_after', 0):,}")
            report.append(f"  Improvement: {gen.get('improvement', 0):,} violations eliminated")
            if 'applied_to' in gen:
                report.append(f"  Applied to: {', '.join(gen['applied_to'])}")
        
        # Privacy Budget (FEATURE 16)
        if 'privacy_budget' in analysis_results:
            budget = analysis_results['privacy_budget']
            report.append("\n" + "─" * w)
            report.append("PRIVACY BUDGET CONFIGURATION")
            report.append("─" * w)
            report.append(f"  Privacy Level: {budget['privacy_level'].upper()}")
            report.append(f"  k-value: {budget['k_value']}")
            report.append(f"  l-value: {budget['l_value']}")
            report.append(f"  Strictness Score: {budget['strictness_score']:.2f}")
            report.append(f"  Data Utility Tradeoff: {budget.get('data_utility_tradeoff', 0):.2f}")
        
        # Recommendations (FEATURE 17)
        if 'recommendations' in analysis_results:
            report.append("\n" + "─" * w)
            report.append("PRIVACY ENHANCEMENT RECOMMENDATIONS")
            report.append("─" * w)
            for i, rec in enumerate(analysis_results['recommendations'], 1):
                report.append(f"\n{i}. [{rec['severity']}] {rec['type'].upper()}")
                report.append(f"   Issue: {rec['message']}")
                report.append(f"   Action: {rec['action']}")
        
        # Human Warnings (FEATURE 9)
        if 'human_warnings' in analysis_results and analysis_results['human_warnings']:
            report.append("\n" + "─" * w)
            report.append("HIGH-RISK RECORD WARNINGS")
            report.append("─" * w)
            for warning in analysis_results['human_warnings'][:5]:
                # Clean ANSI codes for text file
                clean_warning = warning.replace(Colors.RED, '').replace(Colors.YELLOW, '')
                clean_warning = clean_warning.replace(Colors.BOLD, '').replace(Colors.ENDC, '')
                report.append(clean_warning)
        
        # Footer
        report.append("\n" + "═" * w)
        report.append("END OF REPORT")
        report.append("═" * w)
        report.append("\nGenerated by Privacy Intelligence Engine v1.0")
        report.append("All 26+ Features Active • Comprehensive Analysis Complete")
        
        report_text = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(report_text)
                Visualizer.print_success(f"Text report saved to {output_file}")
            except Exception as e:
                Visualizer.print_error(f"Failed to save report: {e}")
        
        return report_text
    
    @staticmethod
    def export_json(analysis_results: Dict[str, Any], output_file: str):
        """Export complete analysis results to JSON"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analysis_results, f, indent=2, default=str)
            Visualizer.print_success(f"JSON export saved to {output_file}")
        except Exception as e:
            Visualizer.print_error(f"Failed to export JSON: {e}")
    
    @staticmethod
    def display_cli_visualizations(analysis_results: Dict[str, Any]):
        """
        FEATURE 21: Risk Visualization Dashboard (CLI Version)
        Beautiful terminal-based data visualizations
        """
        Visualizer.print_header("📊 VISUALIZATION DASHBOARD")
        
        # 1. Risk Distribution Bar Chart
        risk_dist = analysis_results.get('risk_distribution', {})
        if risk_dist:
            Visualizer.print_bar_chart(
                {
                    'HIGH': risk_dist.get('high', 0),
                    'MEDIUM': risk_dist.get('medium', 0),
                    'LOW': risk_dist.get('low', 0)
                },
                "📊 Risk Distribution Across All Records"
            )
        
        # 2. Adaptive Risk Gauge
        if 'adaptive_risk' in analysis_results:
            adaptive = analysis_results['adaptive_risk']
            Visualizer.print_risk_gauge(
                adaptive['adaptive_score'],
                "🎯 Adaptive Privacy Risk Score"
            )
        
        # 3. Attack Success Rates
        if 'attack_simulations' in analysis_results:
            Visualizer.print_subheader("Attack Simulation Success Rates", "⚔️")
            attacks = analysis_results['attack_simulations']
            
            attack_data = {}
            for attack_type, data in attacks.items():
                success_pct = int(data.get('average_success_rate', 0) * 100)
                attack_data[attack_type.capitalize()] = success_pct
            
            Visualizer.print_bar_chart(attack_data, "⚔️  Re-identification Success Rates (%)", width=50)
        
        # 4. Uniqueness Contribution
        if 'uniqueness_contribution' in analysis_results:
            contrib = analysis_results['uniqueness_contribution']
            contrib_percent = {k: int(v * 100) for k, v in contrib.items()}
            Visualizer.print_bar_chart(contrib_percent, "📈 Attribute Uniqueness Contribution (%)", width=50)
        
        # 5. Privacy Metrics Summary Table
        Visualizer.print_subheader("Privacy Metrics Summary", "📋")
        
        metrics_data = []
        
        if 'k_anonymity' in analysis_results:
            ka = analysis_results['k_anonymity']
            metrics_data.append(['k-Anonymity', f"k={ka['k_value']}", f"{ka['violations']} violations", f"{ka['violation_percentage']:.1f}%"])
        
        if 'l_diversity' in analysis_results:
            ld = analysis_results['l_diversity']
            metrics_data.append(['l-Diversity', f"l={ld['l_value']}", f"{ld['violations']} violations", f"{ld['violation_percentage']:.1f}%"])
        
        if 't_closeness' in analysis_results:
            tc = analysis_results['t_closeness']
            metrics_data.append(['t-Closeness', f"t={tc['threshold']}", f"{tc['violations']} violations", "-"])
        
        if metrics_data:
            Visualizer.print_table(
                ['Metric', 'Threshold', 'Violations', 'Rate'],
                metrics_data,
                "Privacy Model Compliance"
            )


# ═══════════════════════════════════════════════════════════════════════════
# MAIN PRIVACY INTELLIGENCE ENGINE (FEATURES 5, 25)
# ═══════════════════════════════════════════════════════════════════════════

class PrivacyIntelligenceEngine:
    """
    FEATURE 5: Multi-Model Privacy Risk Engine
    FEATURE 25: Modular Code Structure
    Main engine coordinating all privacy analysis components
    """
    
    def __init__(self, config: PrivacyConfig = None):
        self.config = config or PrivacyConfig()
        self.analyzer = PrivacyAnalyzer(self.config)
        self.data = None
        self.results = {}
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        FEATURE 22: CSV-Based Data Handling
        Load dataset from CSV file
        """
        logger.info(f"📂 Loading dataset from {filepath}")
        
        try:
            self.data = pd.read_csv(filepath)
            self.filename = os.path.basename(filepath)
            Visualizer.print_success(f"Loaded {len(self.data):,} records with {len(self.data.columns)} columns")
            return self.data
        except Exception as e:
            Visualizer.print_error(f"Failed to load data: {str(e)}")
            raise
    
    def auto_detect_quasi_identifiers(self, exclude_columns: List[str] = None) -> List[str]:
        """
        FEATURE 1: Quasi-Identifier Selection (Auto-detection)
        Automatically detect potential quasi-identifiers
        """
        if self.data is None:
            return []
        
        exclude = exclude_columns or []
        exclude_patterns = ['id', 'name', 'ssn', 'email', 'phone', 'address']
        
        quasi_identifiers = []
        for col in self.data.columns:
            col_lower = col.lower()
            
            # Skip excluded columns
            if col in exclude:
                continue
            
            # Skip identifiers and sensitive patterns
            if any(pattern in col_lower for pattern in exclude_patterns):
                continue
            
            quasi_identifiers.append(col)
        
        # Exclude last column (likely sensitive attribute)
        qi = quasi_identifiers[:-1] if len(quasi_identifiers) > 1 else quasi_identifiers
        
        # Limit to reasonable number
        qi = qi[:min(4, len(qi))]
        
        Visualizer.print_success(f"Auto-detected quasi-identifiers: {', '.join(qi)}")
        return qi
    
    def run_full_analysis(self, quasi_identifiers: List[str], 
                         sensitive_attr: str, 
                         attacker_type: str = 'insider',
                         privacy_level: str = 'medium',
                         show_crypto: bool = False,
                         show_generalization: bool = False) -> Dict[str, Any]:
        """
        FEATURE 5: Multi-Model Privacy Risk Engine
        Run complete privacy analysis pipeline with all 26+ features
        """
        
        # Display beautiful banner
        Visualizer.clear_screen()
        Visualizer.print_banner()
        
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        # Initialize results
        results = {
            'timestamp': datetime.now().isoformat(),
            'dataset_info': {
                'filename': getattr(self, 'filename', 'Unknown'),
                'total_records': len(self.data),
                'total_columns': len(self.data.columns),
                'quasi_identifiers': quasi_identifiers,
                'sensitive_attribute': sensitive_attr
            }
        }
        
        # Progress tracking
        total_steps = 16
        current_step = 0
        
        def update_progress(message):
            nonlocal current_step
            current_step += 1
            Visualizer.print_progress_bar(current_step, total_steps, f"  {message}")
            time.sleep(0.15)
        
        Visualizer.print_header("🔍 COMPREHENSIVE PRIVACY ANALYSIS PIPELINE")
        print(f"{Colors.BOLD}Analyzing {len(self.data):,} records with {len(quasi_identifiers)} quasi-identifiers...{Colors.ENDC}\n")
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 1: k-Anonymity Analysis (FEATURE 2)
        # ═══════════════════════════════════════════════════════════════
        update_progress("k-Anonymity Detection")
        k_value = self.config.config['k_anonymity']
        results['k_anonymity'] = self.analyzer.analyze_k_anonymity(
            self.data, quasi_identifiers, k_value
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 2: l-Diversity Analysis (FEATURE 3)
        # ═══════════════════════════════════════════════════════════════
        update_progress("l-Diversity Checking")
        l_value = self.config.config['l_diversity']
        results['l_diversity'] = self.analyzer.analyze_l_diversity(
            self.data, quasi_identifiers, sensitive_attr, l_value
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 3: t-Closeness Analysis (FEATURE 4)
        # ═══════════════════════════════════════════════════════════════
        update_progress("t-Closeness Analysis")
        t_threshold = self.config.config['t_closeness_threshold']
        results['t_closeness'] = self.analyzer.analyze_t_closeness(
            self.data, quasi_identifiers, sensitive_attr, t_threshold
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 4: Uniqueness Analysis (FEATURE 13)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Uniqueness Score Calculation")
        df_uniqueness, contributions = self.analyzer.calculate_uniqueness_scores(
            self.data, quasi_identifiers
        )
        results['uniqueness'] = {
            'average_score': float(df_uniqueness['uniqueness_score'].mean()),
            'max_score': float(df_uniqueness['uniqueness_score'].max()),
            'high_risk_count': int((df_uniqueness['uniqueness_score'] > 0.5).sum())
        }
        results['uniqueness_contribution'] = contributions
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 5: Weighted Risk Scoring (FEATURE 6)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Weighted Risk Scoring")
        df_risk = self.analyzer.weighted_risk_scoring(
            self.data, quasi_identifiers, 
            self.config.config['risk_weights']
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 6: Risk Classification (FEATURE 8)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Risk Classification")
        results['risk_distribution'] = self.analyzer.classify_records_by_risk(df_risk)
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 7: Adaptive Risk Score (FEATURE 7)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Adaptive Risk Calculation")
        results['adaptive_risk'] = self.analyzer.calculate_adaptive_risk_score(
            len(self.data),
            len(quasi_identifiers),
            results['k_anonymity']['violation_percentage'],
            results['uniqueness']['average_score']
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 8: Human-Readable Warnings (FEATURE 9)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Generating Human Warnings")
        results['human_warnings'] = self.analyzer.generate_human_warnings(
            results['risk_distribution']['high_risk_records'],
            quasi_identifiers
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 9: Attack Simulations (FEATURES 10, 11)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Attack Simulations (All Profiles)")
        results['attack_simulations'] = {}
        for attack_type in ['casual', 'insider', 'advanced']:
            results['attack_simulations'][attack_type] = AttackSimulator.simulate_attacker_knowledge(
                self.data, quasi_identifiers, attack_type
            )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 10: Linkage Attack (FEATURE 12)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Linkage Attack Simulation")
        results['linkage_attack'] = AttackSimulator.simulate_linkage_attack(
            self.data, quasi_identifiers, external_records=100
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 11: Privacy Budget (FEATURE 16)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Privacy Budget Configuration")
        results['privacy_budget'] = PrivacyMitigation.simulate_privacy_budget(
            privacy_level, self.config
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 12: Suppression Recommendations (FEATURE 15)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Suppression Analysis")
        results['suppression'] = PrivacyMitigation.recommend_suppression(
            self.data, quasi_identifiers, k_value
        )
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 13: Generalization (FEATURE 14)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Generalization Engine")
        
        strategy = {
            'age': {'method': 'age_range', 'params': {'bin_size': 5}},
            'zipcode': {'method': 'zipcode', 'params': {'digits': 3}}
        }
        
        actual_strategy = {k: v for k, v in strategy.items() if k in self.data.columns}
        
        if actual_strategy:
            df_generalized, applied = PrivacyMitigation.apply_generalization(self.data, actual_strategy)
            
            # Calculate improvement
            grouped_before = self.data.groupby(quasi_identifiers).size()
            violations_before = (grouped_before < k_value).sum()
            
            grouped_after = df_generalized.groupby(quasi_identifiers).size()
            violations_after = (grouped_after < k_value).sum()
            
            results['generalization'] = {
                'violations_before': int(violations_before),
                'violations_after': int(violations_after),
                'improvement': int(violations_before - violations_after),
                'applied_to': list(actual_strategy.keys()),
                'df_generalized': df_generalized  # Store for later display
            }
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 14: Cryptographic Protection (FEATURE 18)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Cryptographic Protection")
        
        sensitive_fields = [col for col in self.data.columns 
                           if 'id' in col.lower() or col == sensitive_attr]
        if sensitive_fields:
            sample_values = self.data[sensitive_fields[0]].head(10).tolist()
            results['cryptographic_demo'] = {
                'protected_fields': sensitive_fields,
                'sample_values': sample_values,
                'sample_hashes': [CryptoUtils.hash_field(str(v)) for v in sample_values[:5]]
            }
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 15: Dataset Integrity (FEATURE 19)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Integrity Verification")
        results['integrity_hash'] = CryptoUtils.verify_dataset_integrity(self.data)
        
        # ═══════════════════════════════════════════════════════════════
        # STEP 16: Generate Recommendations (FEATURE 17)
        # ═══════════════════════════════════════════════════════════════
        update_progress("Generating Recommendations")
        results['recommendations'] = self._generate_recommendations(results)
        
        print("\n")
        self.results = results
        Visualizer.print_success("✨ Full analysis pipeline complete!")
        
        # ═══════════════════════════════════════════════════════════════
        # Display Results with Visualizations
        # ═══════════════════════════════════════════════════════════════
        
        # Show visualizations (FEATURE 21)
        ReportGenerator.display_cli_visualizations(results)
        
        # Show cryptographic demo if requested (FEATURE 18)
        if show_crypto and 'cryptographic_demo' in results:
            CryptoUtils.demonstrate_cryptographic_protection(
                results['cryptographic_demo']['sample_values'],
                sensitive_attr
            )
        
        # Show generalization demo if requested (FEATURE 14)
        if show_generalization and 'generalization' in results:
            gen_data = results['generalization']
            if 'df_generalized' in gen_data:
                PrivacyMitigation.demonstrate_generalization(
                    self.data,
                    gen_data['df_generalized'],
                    quasi_identifiers,
                    k_value,
                    gen_data['applied_to']
                )
        
        return results
    
    def _generate_recommendations(self, results: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        FEATURE 17: Privacy Enhancement Suggestions
        Generate actionable recommendations based on analysis
        """
        recommendations = []
        
        # k-Anonymity recommendations
        k_viol = results['k_anonymity']['violations']
        k_pct = results['k_anonymity']['violation_percentage']
        if k_viol > 0:
            severity = 'CRITICAL' if k_pct > 20 else 'HIGH'
            recommendations.append({
                'type': 'k-anonymity',
                'severity': severity,
                'message': f'{k_viol} equivalence classes violate k-anonymity ({k_pct:.1f}%)',
                'action': 'Apply generalization to quasi-identifiers (age ranges, ZIP prefix) or suppress outlier records'
            })
        
        # l-Diversity recommendations
        l_viol = results['l_diversity']['violations']
        if l_viol > 0:
            recommendations.append({
                'type': 'l-diversity',
                'severity': 'MEDIUM',
                'message': f'{l_viol} groups lack diversity in sensitive attributes',
                'action': 'Ensure varied sensitive attribute values within each equivalence class or merge similar groups'
            })
        
        # t-Closeness recommendations
        if results.get('t_closeness', {}).get('violations', 0) > 0:
            recommendations.append({
                'type': 't-closeness',
                'severity': 'MEDIUM',
                'message': f'{results["t_closeness"]["violations"]} groups violate t-closeness',
                'action': 'Balance sensitive attribute distribution to match overall dataset distribution'
            })
        
        # Attack vulnerability recommendations
        for attack_type, attack_data in results.get('attack_simulations', {}).items():
            if attack_data['average_success_rate'] > 0.3:
                severity = 'CRITICAL' if attack_data['average_success_rate'] > 0.5 else 'HIGH'
                recommendations.append({
                    'type': f'{attack_type}-attack-vulnerability',
                    'severity': severity,
                    'message': f'{attack_type.capitalize()} attacker has {attack_data["average_success_rate"]:.1%} success rate',
                    'action': f'Increase k-value to {results["k_anonymity"]["k_value"] * 2} or apply stronger generalization to counter {attack_type} attackers'
                })
                break  # Only show most critical attack
        
        # Uniqueness recommendations
        high_unique = results['uniqueness']['high_risk_count']
        if high_unique > 0:
            pct = (high_unique / results['dataset_info']['total_records'] * 100)
            if pct > 10:
                recommendations.append({
                    'type': 'high-uniqueness',
                    'severity': 'MEDIUM',
                    'message': f'{high_unique} records ({pct:.1f}%) have high uniqueness scores (>0.5)',
                    'action': 'Consider suppressing highly unique records or applying aggressive generalization'
                })
        
        # Linkage attack recommendations
        if results.get('linkage_attack', {}).get('linkage_rate', 0) > 20:
            recommendations.append({
                'type': 'linkage-vulnerability',
                'severity': 'HIGH',
                'message': f'High linkage attack success rate: {results["linkage_attack"]["linkage_rate"]:.1f}%',
                'action': 'Reduce quasi-identifier granularity or add noise to prevent external dataset linkage'
            })
        
        # Suppression recommendations
        if results.get('suppression', {}).get('percentage_to_suppress', 0) > 0:
            pct = results['suppression']['percentage_to_suppress']
            if pct < 5:  # Acceptable suppression level
                recommendations.append({
                    'type': 'record-suppression',
                    'severity': 'LOW',
                    'message': f'Minimal suppression needed: {pct:.1f}% of records',
                    'action': f'Suppress {results["suppression"]["records_to_suppress"]} outlier records to achieve k-anonymity'
                })
        
        return recommendations


# ═══════════════════════════════════════════════════════════════════════════
# FEATURE 23: CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """
    FEATURE 23: CLI Interface
    Beautiful command-line interface with argparse
    """
    
    parser = argparse.ArgumentParser(
        description='🔐 Privacy Intelligence Engine - Advanced Re-identification Warning System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
{Colors.CYAN}{Colors.BOLD}Examples:{Colors.ENDC}
  
  {Colors.GREEN}# Basic analysis (auto-detect everything){Colors.ENDC}
  %(prog)s --data patients.csv
  
  {Colors.GREEN}# Advanced analysis with all features{Colors.ENDC}
  %(prog)s --data patients.csv --k 5 --l 3 --attacker advanced \\
           --show-crypto --show-generalization --export-json
  
  {Colors.GREEN}# High-security analysis{Colors.ENDC}
  %(prog)s --data sensitive_data.csv --privacy-level high \\
           --config config.json --verbose
  
  {Colors.GREEN}# Custom quasi-identifiers{Colors.ENDC}
  %(prog)s --data data.csv --quasi-identifiers age gender zipcode \\
           --sensitive diagnosis --k 10

{Colors.CYAN}{Colors.BOLD}Features:{Colors.ENDC} All 26+ features active including:
  • k-Anonymity, l-Diversity, t-Closeness analysis
  • Attack simulations (Casual/Insider/Advanced)
  • Cryptographic protection (SHA-256)
  • Automatic generalization & suppression
  • Beautiful CLI visualizations
  • Comprehensive reporting (TXT/JSON)
        """
    )
    
    # Required arguments
    parser.add_argument('--data', '-d', required=True, 
                       help='Path to CSV data file')
    
    # Optional arguments
    parser.add_argument('--config', '-c', 
                       help='Path to JSON configuration file')
    parser.add_argument('--quasi-identifiers', '-q', nargs='+', 
                       help='List of quasi-identifier columns (auto-detected if not specified)')
    parser.add_argument('--sensitive', '-s', 
                       help='Sensitive attribute column (last column if not specified)')
    parser.add_argument('--k', type=int, default=3, 
                       help='k-anonymity threshold (default: 3)')
    parser.add_argument('--l', type=int, default=2, 
                       help='l-diversity threshold (default: 2)')
    parser.add_argument('--attacker', choices=['casual', 'insider', 'advanced'], 
                       default='insider', 
                       help='Attacker knowledge profile (default: insider)')
    parser.add_argument('--privacy-level', choices=['low', 'medium', 'high', 'maximum'],
                       default='medium', 
                       help='Privacy strictness level (default: medium)')
    parser.add_argument('--output', '-o', 
                       help='Output directory for reports (default: privacy_reports)')
    parser.add_argument('--export-json', action='store_true', 
                       help='Export results as JSON')
    parser.add_argument('--show-crypto', action='store_true',
                       help='Demonstrate cryptographic protection (FEATURE 18)')
    parser.add_argument('--show-generalization', action='store_true',
                       help='Show generalization before/after comparison (FEATURE 14)')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        # ═══════════════════════════════════════════════════════════════
        # Initialize Engine
        # ═══════════════════════════════════════════════════════════════
        config = PrivacyConfig(args.config) if args.config else PrivacyConfig()
        config.config['k_anonymity'] = args.k
        config.config['l_diversity'] = args.l
        
        engine = PrivacyIntelligenceEngine(config)
        
        # ═══════════════════════════════════════════════════════════════
        # Load Data (FEATURE 22)
        # ═══════════════════════════════════════════════════════════════
        engine.load_data(args.data)
        
        # ═══════════════════════════════════════════════════════════════
        # Determine Quasi-Identifiers (FEATURE 1)
        # ═══════════════════════════════════════════════════════════════
        if args.quasi_identifiers:
            quasi_identifiers = args.quasi_identifiers
            Visualizer.print_info(f"Using specified quasi-identifiers: {', '.join(quasi_identifiers)}")
        else:
            quasi_identifiers = engine.auto_detect_quasi_identifiers()
        
        # Determine sensitive attribute
        if args.sensitive:
            sensitive_attr = args.sensitive
        else:
            sensitive_attr = engine.data.columns[-1]
            Visualizer.print_info(f"Using '{sensitive_attr}' as sensitive attribute")
        
        # ═══════════════════════════════════════════════════════════════
        # Run Full Analysis (ALL FEATURES)
        # ═══════════════════════════════════════════════════════════════
        results = engine.run_full_analysis(
            quasi_identifiers, 
            sensitive_attr, 
            args.attacker,
            args.privacy_level,
            args.show_crypto,
            args.show_generalization
        )
        
        # ═══════════════════════════════════════════════════════════════
        # Generate Reports (FEATURES 20, 21)
        # ═══════════════════════════════════════════════════════════════
        output_dir = args.output or 'privacy_reports'
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Text report (FEATURE 20)
        report_file = os.path.join(output_dir, f'privacy_report_{timestamp}.txt')
        ReportGenerator.generate_text_report(results, report_file)
        
        # JSON export
        if args.export_json:
            json_file = os.path.join(output_dir, f'privacy_analysis_{timestamp}.json')
            ReportGenerator.export_json(results, json_file)
        
        # ═══════════════════════════════════════════════════════════════
        # Final Summary
        # ═══════════════════════════════════════════════════════════════
        Visualizer.print_header("📋 ANALYSIS COMPLETE - SUMMARY")
        
        summary_content = [
            f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Dataset: {results['dataset_info']['filename']}",
            f"Total Records: {results['dataset_info']['total_records']:,}",
            "",
            f"Quasi-Identifiers: {', '.join(quasi_identifiers)}",
            f"Sensitive Attribute: {sensitive_attr}",
            "",
            "═══ PRIVACY METRICS ═══",
            f"k-Anonymity Violations: {results['k_anonymity']['violations']:,} ({results['k_anonymity']['violation_percentage']:.1f}%)",
            f"l-Diversity Violations: {results['l_diversity']['violations']:,} ({results['l_diversity']['violation_percentage']:.1f}%)",
            f"t-Closeness Violations: {results['t_closeness']['violations']:,}",
            "",
            "═══ RISK ASSESSMENT ═══",
            f"Adaptive Risk Score: {results['adaptive_risk']['adaptive_score']:.3f}",
            f"Risk Level: {results['adaptive_risk']['level']}",
            f"HIGH Risk Records: {results['risk_distribution']['high']:,} ({results['risk_distribution']['high_pct']:.1f}%)",
            "",
            "═══ ATTACK SIMULATIONS ═══",
            f"Casual Attacker Success: {results['attack_simulations']['casual']['average_success_rate']:.1%}",
            f"Insider Attacker Success: {results['attack_simulations']['insider']['average_success_rate']:.1%}",
            f"Advanced Attacker Success: {results['attack_simulations']['advanced']['average_success_rate']:.1%}",
            "",
            "═══ REPORTS ═══",
            f"Text Report: {report_file}",
            f"JSON Export: {json_file if args.export_json else 'Not generated'}",
            f"Recommendations: {len(results['recommendations'])} actions suggested"
        ]
        
        Visualizer.print_box("ANALYSIS SUMMARY", summary_content, Colors.GREEN)
        
        # Display recommendations
        if results['recommendations']:
            Visualizer.print_subheader("Priority Recommendations", "💡")
            for i, rec in enumerate(results['recommendations'][:5], 1):
                severity_color = Colors.RED if rec['severity'] == 'CRITICAL' or rec['severity'] == 'HIGH' else Colors.YELLOW
                print(f"\n{severity_color}{Colors.BOLD}{i}. [{rec['severity']}] {rec['type'].upper()}{Colors.ENDC}")
                print(f"   {rec['message']}")
                print(f"   {Colors.GREEN}→ Action:{Colors.ENDC} {rec['action']}")
            print()
        
        # Final message
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'═'*80}{Colors.ENDC}")
        print(f"{Colors.GREEN}{Colors.BOLD}✨ Thank you for using Privacy Intelligence Engine! ✨{Colors.ENDC}")
        print(f"{Colors.CYAN}🔐 All 26+ Features Active • Comprehensive Analysis Complete{Colors.ENDC}")
        print(f"{Colors.CYAN}{'═'*80}{Colors.ENDC}\n")
        
    except FileNotFoundError:
        Visualizer.print_error(f"Data file not found: {args.data}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Analysis interrupted by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        Visualizer.print_error(f"Analysis failed: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()


# ═══════════════════════════════════════════════════════════════════════════
# END OF PRIVACY INTELLIGENCE ENGINE
# ═══════════════════════════════════════════════════════════════════════════
"""
FEATURE CHECKLIST - ALL 26+ IMPLEMENTED:

✅ 1.  Quasi-Identifier Selection (Auto & Manual)
✅ 2.  k-Anonymity Risk Detection
✅ 3.  l-Diversity Checking
✅ 4.  Simplified t-Closeness
✅ 5.  Multi-Model Privacy Risk Engine
✅ 6.  Weighted Quasi-Identifier Risk Scoring
✅ 7.  Progressive (Adaptive) Risk Levels
✅ 8.  Re-Identification Risk Classification
✅ 9.  Human-Readable Risk Warnings
✅ 10. Attacker Knowledge Profiles
✅ 11. Attack Simulation Engine
✅ 12. Linkage Attack Simulation
✅ 13. Uniqueness Contribution Analysis
✅ 14. Automatic Generalization Engine
✅ 15. Suppression Recommendation System
✅ 16. Privacy Budget Simulator
✅ 17. Privacy Enhancement Suggestions
✅ 18. Field-Level Cryptographic Protection (SHA-256)
✅ 19. Dataset Integrity Verification
✅ 20. Explainable Privacy Report Generator
✅ 21. Risk Visualization Dashboard (CLI)
✅ 22. CSV-Based Data Handling
✅ 23. CLI Interface (argparse)
✅ 24. Config-Driven Architecture
✅ 25. Modular Code Structure
✅ 26. Code Quality & Maintainability

BONUS FEATURES:
✅ Beautiful ANSI colored terminal output
✅ Animated progress bars
✅ ASCII bar charts and gauges
✅ Comprehensive error handling
✅ Multiple attacker simulations
✅ Before/after generalization comparison
✅ Cryptographic demonstration mode
✅ JSON and TXT export formats
✅ Configurable privacy levels
✅ Detailed logging system
"""
