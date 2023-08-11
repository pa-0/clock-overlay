# clock-overlay

This is a Windows 10 App for displaying the system time on top of other applications, except in fullscreen.

Developed and tested with Windows 10 Pro (v10.0.19045).

## Setup

Make sure you have Python v3.11 (or higher) and TkInter installed.

Clone this repository, cd into it and execute the following command;

> pip install -e .

## Usage

Open Windows Run and execute the following command:

> powershell Start-Process -WindowStyle "Hidden" clock-overlay

This will open the application without a console window. Press the middle mouse button to quit.
