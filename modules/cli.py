import argparse
from modules.audit import run as audit_run
from modules.configuration import run as config_run
from modules.deployment import run as deployment_run
from modules.file_backup import run as backup_run
from modules.logs import run as logs_run
from modules.monitoring import run as monitor_run
from modules.package_manager import run as package_manager_run
from modules.process_service import run as process_service_run
from modules.reporting import run as reporting_run
from modules.scheduler import run as scheduler_run
from modules.storage_cleanup import run as storage_cleanup_run
from modules.users import run as users_run

def create_parser():
    # creates the main CLI 
    parser = argparse.ArgumentParser(prog="DevOps Automation Suite", description="A CLI tool to automate common DevOps tasks.")

    # creates space for commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    audit_parser = subparsers.add_parser("audit", help="Run infrastructure audit")
    # link command to function
    audit_parser.set_defaults(func=audit_run)

    config_parser = subparsers.add_parser("config", help="Manage configurations")
    config_parser.set_defaults(func=config_run)

    deploy_parser = subparsers.add_parser("deploy", help="Automate deployment and Git operations")
    deploy_parser.set_defaults(func=deployment_run)

    backup_parser = subparsers.add_parser("backup", help="Manage files, directories, backup and restore")
    backup_parser.set_defaults(func=backup_run)

    logs_parser = subparsers.add_parser("logs", help="Analyze Linux log files")
    logs_parser.set_defaults(func=logs_run)

    monitor_parser = subparsers.add_parser("monitor", help="CPU, RAM, Disk, Network and system resources")
    monitor_parser.set_defaults(func=monitor_run)

    package_parser = subparsers.add_parser("packages", help="Manage software packages and environment variables")
    package_parser.set_defaults(func=package_manager_run)

    process_service_parser = subparsers.add_parser("process", help="Manage processes and system services")
    process_service_parser.set_defaults(func=process_service_run)

    reporting_parser = subparsers.add_parser("report", help="Generate reports")
    reporting_parser.set_defaults(func=reporting_run)

    schedule_parser = subparsers.add_parser("schedule", help="Schedule automation tasks using cron")
    schedule_parser.set_defaults(func=scheduler_run)

    storage_parser = subparsers.add_parser("storage", help="Analyze storage and perform cleanup")
    storage_parser.set_defaults(func=storage_cleanup_run)

    users_parser = subparsers.add_parser("users", help="Manage users, groups and permissions")
    users_parser.set_defaults(func=users_run)
    
    return parser
