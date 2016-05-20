# natas 10
used [xor-kpa.py](https://blog.didierstevens.com/2016/01/01/xor-known-plaintext-attack/) to find the key using a known plaintext (our cookies)

```
$ ./xor-kpa.py ciphert plaint
Key:       qw8J
Extra:     37
Keystream: qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
```

plaint simply being the json encoded result from php:

```
$ php -a
php > echo(json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff")));
{"showpassword":"no","bgcolor":"#ffffff"}
```
