class Solution:

        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def dfs(accno, emails):
            if self.visited_acc[accno]:
                return
            self.visited_acc[accno]=True
            for j in range(1, len(accounts[accno])):
                email = accounts[accno][j]
                emails.add(email)
                for each_accno in self.dic_email[email]:
                    dfs(each_accno, emails)
           
        self.dic_email = collections.defaultdict(list)
        self.visited_acc = [False]*len(accounts)
        ans = [] 
        
        for i, acc in enumerate(accounts):
            name = acc[0]
            emails = acc[1:]
            for email in emails:
                self.dic_email[email].append(i)
        print(self.dic_email)
        
        for i, acc in enumerate(accounts):
            if self.visited_acc[i]==True:
                continue
            name = acc[0]
            emails = set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))
        return ans
                
