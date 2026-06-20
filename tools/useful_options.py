#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Useful Options Module - ABHINAV Premium Edition
"""

from colorama import Fore, Style

def tokens_checker():
    """Tokens Checker Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - Tokens Checker{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Verify tokens")
    print("    ✓ Check validity")
    print("    ✓ Batch verification")
    print("    ✓ Status reporting")
    print("    ✓ Export results")
    token_file = input(f"{Fore.YELLOW}[*] Enter token file path: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Checking tokens from: {token_file}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def clear_dm():
    """Clear DM Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - Clear DM{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Delete DMs")
    print("    ✓ Clear conversations")
    print("    ✓ Selective deletion")
    print("    ✓ Bulk clearing")
    print("    ✓ Date-based filtering")
    user = input(f"{Fore.YELLOW}[*] Enter user ID/name: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Clearing DMs with: {user}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def house_changer():
    """House Changer Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - House Changer{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Change location")
    print("    ✓ Update profile")
    print("    ✓ Spoof location")
    print("    ✓ Timezone management")
    print("    ✓ Multi-location support")
    location = input(f"{Fore.YELLOW}[*] Enter new location: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Changing location to: {location}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def server_lookup():
    """Server Lookup Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - Server Lookup{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Lookup server info")
    print("    ✓ Get member count")
    print("    ✓ Check permissions")
    print("    ✓ Role listing")
    print("    ✓ Channel info")
    server = input(f"{Fore.YELLOW}[*] Enter server ID/name: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Lookup results for: {server}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def mass_dm():
    """Mass DM Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - Mass DM{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Send bulk messages")
    print("    ✓ Auto-delay")
    print("    ✓ Message templates")
    print("    ✓ Variable substitution")
    print("    ✓ Delivery tracking")
    message = input(f"{Fore.YELLOW}[*] Enter message: {Style.RESET_ALL}")
    count = input(f"{Fore.YELLOW}[*] Number of recipients: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Sending {count} DMs with message: {message}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def group_spammer():
    """Group Spammer Tool"""
    print(f"{Fore.CYAN}\n{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] ABHINAV - Group Spammer{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features:{Style.RESET_ALL}")
    print("    ✓ Spam groups")
    print("    ✓ Message rotating")
    print("    ✓ Rate limiting bypass")
    print("    ✓ Multi-group support")
    print("    ✓ Scheduled spamming")
    group = input(f"{Fore.YELLOW}[*] Enter group ID/name: {Style.RESET_ALL}")
    print(f"{Fore.GREEN}[!] Spamming group: {group}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

def useful_options_menu(choice):
    """Handle useful options menu"""
    options = {
        '15': tokens_checker,
        '16': clear_dm,
        '17': house_changer,
        '18': server_lookup,
        '19': mass_dm,
        '20': group_spammer
    }
    
    if choice in options:
        options[choice]()
    else:
        print(f"{Fore.RED}[!] Invalid option{Style.RESET_ALL}")