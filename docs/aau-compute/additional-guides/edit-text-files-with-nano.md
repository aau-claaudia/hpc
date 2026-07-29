The most beginner-friendly text editor commonly found on Linux systems is Nano.

Opening the file `my_file` can be done by saing:

```bash
nano my_file
```

This will open up the text editor, which should look like:

<div class="fixed-width-4-nano">
```text { .yaml .no-copy }
  GNU nano 4.8                                 my_file                                      











^G Get Help   ^O Write Out  ^W Where Is   ^K Cut Text   ^J Justify    ^C Cur Pos    M-U Undo
^X Exit       ^R Read File  ^\ Replace    ^U Paste Text ^T To Spell   ^_ Go To Line M-E Redo

```
</div>

#### Nice to know about Nano:

* Opening Nano without a target file, will open a *buffer* that can be saved and named later (just like opening a blank word document). 
* The two lines at the very bottom of the Nano *interface* will hint at which keyboard shortcuts call which actions.
    * The symbol `^` means ++ctrl++
    * The `M` means ++alt++


| Action                        | Keybind    | Notes |
|                               |            | ------------------------------------ |
| :fontawesome-solid-save: Save | ++ctrl+s++ | You will be asked to confirm, if you wish to save to the current file. If you have not yet named your file, you will be asked to name the file first. Press ++y++ to confirm, or ++n++ to reject |
| :material-close-box: Exit     | ++ctrl+x++ | If you have unsaved changes, you will be asked if you wish to save.|
| :octicons-search-16: Search   | ++ctrl+w++ | Type in your search term, and press ++enter++. To repeat press ++ctrl+w++ and ++enter++ again (the search term is automatically repeated). |
