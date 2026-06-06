# Last updated: 6/6/2026, 10:25:12 PM
class Solution:
    def numUniqueEmails(self,emails):
        unique_emails = []
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            normalized = local + '@' + domain
            if normalized not in unique_emails:
                unique_emails.append(normalized)
        return len(unique_emails)

# Example usage:
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
solution=Solution()
print(solution.numUniqueEmails(emails))  
