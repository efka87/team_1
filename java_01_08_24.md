```java
	
@PostMapping("/balance")
	public Account balance(@RequestBody Credentials credentials) {
		if (credentials.username.equals("usernme") && credentials.password.equals("pass123")) {
			double bankBalance = 10240.50;
			Account account = new Account();
			account.bankBalance = bankBalance;
			return account;
		}
			return null;
	}
```

```java
package com.datorium.Datorium.API;

public class Account {
    public double bankBalance; 
}
```





