<%namespace name="common" file="common.mako" />
<%def name="render()">\
<html>
<body>
    <h1>Welcome</h1>
    <p>${common.greet("Bob")}</p>
</body>
</html>
</%def>\
