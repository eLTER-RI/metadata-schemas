[Back to Menu](main.md)

# Problems

## inotify watch limit reached
**Message**: OSError: [Errno 28] inotify watch limit reached

**Solution**: 
```bash
echo fs.inotify.max_user_watches=524288 | sudo tee /etc/sysctl.d/40-max-user-watches.conf && sudo sysctl --system
```

[Back to Menu](main.md)