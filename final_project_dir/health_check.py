#! /usr/bin/env python3

import shutil
import psutil
import socket
import emails

recipient = "student-00-4094e4e9d9f9@example.com"


def check_disk():
    disk_usage = shutil.disk_usage("/")
    disk_free = disk_usage.free / disk_usage.total * 100

    if disk_free < 20:
        emails.generate_error_report("automation@example.com", recipient,
                                     "Error - Available disk space is less than 20%",
                                     "Please check your system and resolve the issue as soon as possible.")


def check_cpu():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        emails.generate_error_report("automation@example.com", recipient,
                                     "Error - CPU usage is over 80%",
                                     "Please check your system and resolve the issue as soon as possible.")


def check_memory():
    ram_usage = psutil.virtual_memory()
    available_memory = ram_usage.available() // 1024 ** 2
    if available_memory < 500:
        emails.generate_error_report("automation@example.com", recipient,
                                     "Error - Available memory is less than 500MB",
                                     "Please check your system and resolve the issue as soon as possible.")


def check_localhost():
    ip = socket.gethostbyname("localhost")
    if ip != "127.0.0.1":
        emails.generate_error_report("automation@example.com", recipient,
                                     "Error - localhost cannot be resolved to 127.0.0.1",
                                     "Please check your system and resolve the issue as soon as possible.")


if __name__ == "__main__":
    check_disk()
    check_cpu()
    check_memory()
    check_localhost()
