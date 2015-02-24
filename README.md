## Notes

1. Typically, business logic would inform how strict or forgiving the regular expression for validating email addresses should be. In this light, ```\[^@]+@[^@]+\.[^@]+\``` is an arbitrary choice.

2. For brevity, a catch-all is used for the various exceptions raised by ```dnsresolver``` and ```smtplib```.

3. Checking MX records exhaustively is not efficient: a non-existent email address will lead to as many SMTP sever requests as there are records. A better solution may be only to check the record with the highest preference.
