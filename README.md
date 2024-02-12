# download stuff from youtube

## pytube documentation:
https://pytube.io/en/latest/user/quickstart.html

## fix for caption download: 
https://github.com/pytube/pytube/issues/1477

```python
--- captions.py.orig	2023-04-01 03:12:55.176218471 +0200
+++ captions.py	2023-04-01 03:12:59.320187087 +0200
@@ -82,14 +82,14 @@
         """
         segments = []
         root = ElementTree.fromstring(xml_captions)
-        for i, child in enumerate(list(root)):
+        for i, child in enumerate(list(root[0])):
             text = child.text or ""
             caption = unescape(text.replace("\n", " ").replace("  ", " "),)
             try:
-                duration = float(child.attrib["dur"])
+                duration = float(child.attrib["d"]) / 1000.0
             except KeyError:
                 duration = 0.0
-            start = float(child.attrib["start"])
+            start = float(child.attrib["t"]) / 1000.0
             end = start + duration
             sequence_number = i + 1  # convert from 0-indexed to 1.
             line = "{seq}\n{start} --> {end}\n{text}\n".format(
```