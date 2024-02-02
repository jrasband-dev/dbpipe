# dbpipe

A lightweight and easy way to manage data pipelines.

## Creating a Pipe

```python
from dbpipe.core.pipes import Pipe

pipe = Pipe(
        sourceType="MS SQL SERVER",
        sources=["AdSpend","Social Stats"],
        destinationType="MS SQL SERVER",
        destination="DW",
        frequency=None,
        logfile=None,
        filepath="Test.py"
    )

print(pipe)
```

## Saving a Pipe
```python
pipe.save('DW.json')
```
## Lineage

```python
from dbpipe.lineage.mermaid import generate_mermaid_markdown_file

generate_mermaid_markdown_file('pipes','test.md')
```




