def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
    return '%dA%dB' % (bulls, both - bulls)
