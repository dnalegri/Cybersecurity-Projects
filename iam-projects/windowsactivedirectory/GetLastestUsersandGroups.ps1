# Import Active Directory module
Import-Module ActiveDirectory

# Get the latest users created (adjust the number of users you want to see by changing the value of -First)
$latestUsers = Get-ADUser -Filter * -Properties WhenCreated | Sort-Object WhenCreated -Descending | Select-Object Name, SamAccountName, WhenCreated -First 10

# Get the latest groups created (adjust the number of groups you want to see by changing the value of -First)
$latestGroups = Get-ADGroup -Filter * -Properties WhenCreated | Sort-Object WhenCreated -Descending | Select-Object Name, SamAccountName, WhenCreated -First 10

# Display the latest users created
Write-Host "Latest Users Created:"
$latestUsers | Format-Table -AutoSize

# Display the latest groups created
Write-Host "Latest Groups Created:"
$latestGroups | Format-Table -AutoSize
