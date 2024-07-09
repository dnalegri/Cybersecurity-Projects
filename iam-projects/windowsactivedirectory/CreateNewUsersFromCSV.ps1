# Import required modules
Import-Module ActiveDirectory

# Create a new password
$SecurePassword = ConvertTo-SecureString "TESTpassw0rd!" -AsPlainText -Force

# Prompt User for CSV file path
$filepath = Read-Host -Prompt "Please enter the path to your CSV file"

# Import the file into a variable
$users = Import-Csv $filepath

# Loop through each row and gather information
ForEach ($user in $users) {
    # Gather the user's information
    $fname = $user.'First Name'
    $lname = $user.'Last Name'
    $displayname = $user.'Display Name'
    $username = $user.'Username'
    $description = $user.'Description'
    $group = $user.'Group'
    $ou = $user.'OU'

    # Create new AD user for each user in CSV file
    New-ADUser `
        -Name "$fname $lname" `
        -GivenName $fname `
        -Surname $lname `
        -SamAccountName $username `
        -UserPrincipalName ($username + "@yellow.local") `
        -Description $description `
        -Path $ou `
        -AccountPassword $SecurePassword `
        -Enabled $true

    # Set the password to never expire
    Set-ADUser -Identity $username -PasswordNeverExpires $true

    # Add the AD user to group
    Add-ADGroupMember -Identity $group -Members $username

    # Echo the user's first and last name and group
    Write-Host "User $fname $lname has been created and added to group $group."
}

Write-Host "All users have been added successfully."
