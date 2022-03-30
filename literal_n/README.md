## Character to Whitespace (ctow)

Takes input file and replaces '\n' with newline and '\t' with tabs.

Use the -r flag to reverse the output, ie. replace newlines with '\n' and tabs with '\t' 

### Example Usage

With input.txt as: </br>
```
line 1 is\t here\nline2 is\t here\n line3\nis above \tthis
```

`python3 ctow.py input.txt` returns </br>

```
line 1 is        here
line2 is         here
 line3
is above        this
```