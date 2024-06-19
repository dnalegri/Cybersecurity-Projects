
# Windows Defender Security Hardening

This repository contains detailed documentation and scripts for hardening Windows Defender on a Windows 10 Enterprise machine connected to a Windows Server Domain Controller (yellow.local). The hardening was performed using an admin account.

## Overview

The following settings were configured to enhance security:
- Real-time protection
- Cloud-delivered protection
- Automatic sample submission
- Tamper protection
- Controlled folder access (to protect against ransomware)
- Various Group Policy settings for Microsoft Defender Antivirus

> **Note:** Some of these settings may impact system performance.

## Windows Defender Settings

### Real-time Protection
Real-time protection ensures that your device is constantly protected by scanning for malware and other threats in real time.

### Cloud-delivered Protection
Cloud-delivered protection leverages Microsoft's vast cloud-based resources to provide faster and more accurate threat detection.

### Automatic Sample Submission
Automatic sample submission helps Microsoft analyze suspicious files and improve malware detection by sending samples to Microsoft.

### Tamper Protection
Tamper protection prevents malicious changes to important security settings, ensuring that your security configuration remains intact.

### Controlled Folder Access
Controlled folder access helps protect your data from ransomware by blocking unauthorized changes to your protected folders.

## Group Policy Settings

### Microsoft Defender Antivirus (MAPS)

1. **Join Microsoft MAPS (Microsoft Advanced Protection Service)**:
   - **Setting:** Enabled
   - **Level:** Advanced MAPS
   - **Explanation:** Advanced MAPS provides more detailed and comprehensive protection by sharing detailed information about detected threats with Microsoft.

2. **Configure the Block at First Sight Feature**:
   - **Setting:** Enabled
   - **Explanation:** This feature helps to detect and block new malware within seconds by leveraging the power of the cloud.

### MpEngine Settings

1. **Configure Extended Cloud Check**:
   - **Setting:** Enabled
   - **Time:** 20 seconds
   - **Explanation:** This setting extends the time that Defender Antivirus uses to check for a cloud-based response, providing a more thorough analysis.

2. **Cloud Protection Level**:
   - **Setting:** High+ blocking level
   - **Explanation:** The high protection level ensures that more suspicious files and behaviors are analyzed and blocked if necessary, providing enhanced security.

### PowerShell Configuration

- **Command:** `Set-MpPreference -PUAProtection 1`
- **Explanation:** This command enables Potentially Unwanted Application (PUA) protection, which helps to block applications that can cause slowdowns, display unwanted advertisements, or offer to install additional software.

## Performance Impact

**Note:** Enabling these advanced security settings can have an impact on system performance. The trade-off between security and performance should be carefully considered based on your specific needs and environment.

## Steps to Apply the Settings

1. **Enable Windows Defender Settings**:
   - Ensure that real-time protection, cloud-delivered protection, automatic sample submission, and tamper protection are enabled.
   - Turn on controlled folder access.

2. **Edit Group Policy**:
   - Open Group Policy Editor (`gpedit.msc`).
   - Navigate to `Computer Configuration -> Administrative Templates -> Windows Components -> Microsoft Defender Antivirus -> MAPS`.
   - Enable `Join Microsoft MAPS` and set it to `Advanced MAPS`.
   - Enable `Configure the Block at First Sight feature`.

3. **Configure Extended Cloud Check**:
   - Navigate to `Computer Configuration -> Administrative Templates -> Windows Components -> Microsoft Defender Antivirus -> MpEngine`.
   - Enable `Configure extended cloud check` and set it to 20 seconds.
   - Set the cloud protection level to `High+ blocking level`.

4. **Set PUA Protection**:
   - Open PowerShell as an administrator.
   - Run the command: `Set-MpPreference -PUAProtection 1`

## Conclusion

By following these steps, you can significantly enhance the security posture of your Windows 10 Enterprise system. Be mindful of the potential performance impacts and adjust settings as necessary to find the right balance for your environment.
