from bank_accounts import *

Kina = BankAccount(1000, "Kina")
Sara = BankAccount(2000, "Sara")

Kina.getBalance()

Sara.getBalance()
Sara.deposit(500)

Kina.withdraw(10000)
Kina.withdraw(10)
Kina.transfer(10000, Sara)
Kina.transfer(100, Sara)

jim = InterestRewardsAcct(1000, 'Jim')
jim.getBalance()
jim.deposit(100)
jim.transfer(100, Kina)

Sankara = SavingsAcct(1000, "Sankara")
Sankara.getBalance()
Sankara.deposit(100)
Sankara.transfer(10000, Sara)
Sankara.transfer(1000, Sara)