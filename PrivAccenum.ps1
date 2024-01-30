Get-DomainGroupMember -Identity 'Domain Admins' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_DomainAdmins.csv
Get-DomainGroupMember -Identity 'Enterprise Admins' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_EnterpriseAdmins.csv
Get-DomainGroupMember -Identity 'Administrators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_Administrators.csv
Get-DomainGroupMember -Identity 'Account Operators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_AccountOperators.csv
Get-DomainGroupMember -Identity 'AdminSDHolder' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_AdminSDHolder.csv
Get-DomainGroupMember -Identity 'Backup Operators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_BackupOperators.csv
Get-DomainGroupMember -Identity 'DnsAdmins' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_DnsAdmins.csv
Get-DomainGroupMember -Identity 'Event Log Readers' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_EventLogReaders.csv
Get-DomainGroupMember -Identity 'Exchange Windows Permissions' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_ExchWinPerms.csv
Get-DomainGroupMember -Identity 'Hyper-V Administrators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_HyperVAdmins.csv
Get-DomainGroupMember -Identity 'Organization Management' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_OrgManagement.csv
Get-DomainGroupMember -Identity 'Print Operators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_PrintOperators.csv
Get-DomainGroupMember -Identity 'Remote Desktop Users' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_RDUsers.csv
Get-DomainGroupMember -Identity 'Remote Management Users' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_RMUsers.csv
Get-DomainGroupMember -Identity 'Server Operators' -Recurse | select MemberName | Get-DomainUser -Properties * | Export-Csv -Encoding UTF8 -path privacc_ServerOperators.csv
