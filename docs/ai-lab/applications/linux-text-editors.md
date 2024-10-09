##### On AI-LAB, you may need to edit files frequently, whether it's modifying scripts, configuration files, or logs. Two popular command-line text editors are nano and vim. This guide provides an introduction to both editors, covering essential commands and workflows.

## Nano: A Simple Text Editor
Nano is a beginner-friendly text editor. It is easy to use, making it a good choice for new users.

#### Opening a File with Nano
To open or create a file, use:

```
nano <filename>
```

For example, to open `myfile.txt`:

```
nano myfile.txt
```

#### Basic Commands in Nano
Once inside Nano, use the following commands:

* Move the cursor: Use the arrow keys.
* Save the file: Press `Ctrl + O` (Write Out), then hit `Enter`.
* Exit Nano: Press `Ctrl + X`.
* Cut and Paste:
    * To cut: `Ctrl + K` cuts the current line.
    * To paste: `Ctrl + U` pastes the cut text.
* Search within the file: Press `Ctrl + W`, type the search term, and hit `Enter`.

!!! info "Tips for Nano"
    * The commands at the bottom of the Nano screen start with the `^` symbol, which stands for the `Ctrl` key.
    * For more advanced editing, Nano has flags like syntax highlighting and can open files as read-only using the `-v` flag:
    ```
    nano -v myfile.txt
    ```

---

## Vim: A Powerful Text Editor
Vim is a more advanced editor with modes and extensive features. Though it has a steeper learning curve, it's incredibly powerful for experienced users.

#### Opening a File with Vim
To open or create a file in Vim, use:

```
vim <filename>
```

For example, to open `script.sh`:

```
vim script.sh
```

#### Understanding Vim Modes
Vim has different modes, each designed for specific tasks:

* Normal Mode: Used for navigating and executing commands.
* Insert Mode: For typing and editing text.
* Visual Mode: For selecting and manipulating blocks of text.
* You start in Normal Mode by default. Press `i` to enter Insert Mode for text editing.

#### Basic Commands in Vim
| Action | Command |
| --- | --- |
| Enter Insert Mode	| `i` |
| Save the file | `:w` |
| Exit Vim | `:q` |
| Save and Exit | `:wq` or `ZZ` |
| Undo last change | `u` |
| Delete a line | `dd` |
| Copy a line | `yy` |
| Paste a line | `p` |
| Search | `/` followed by search term and `Enter` |

#### Navigating in Vim
* Move the cursor: Use arrow keys or `h` (left), `j` (down), `k` (up), `l` (right).
* Jump to start/end of file: `gg` (start), `G` (end).
* Go to a specific line: `:<line number>`, then `Enter`.

#### Exiting Vim
If you're stuck in Vim and want to exit:

* Force quit without saving: `:q!`
* Save and quit: `:wq` or `ZZ`.

!!! info "Tips for Vim"
    * Vim has a built-in help system, accessed by typing `:help`.
    * You can enable syntax highlighting with the command `:syntax` on.

---

## Summary
| Editor | Easy-to-use | Advanced Features | Quick to Learn |
| --- | --- | --- | --- |
| Nano | Yes | No | Yes |
| Vim | No | Yes | No |

Both editors are available on AI-LAB, so you can choose the one that fits your workflow and experience level. Nano is great for quick edits, while Vim offers advanced capabilities for power users.