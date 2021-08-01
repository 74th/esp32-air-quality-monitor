rsync ./air_quality_monitor /pyboard/air_quality_monitor
# repl ~ import machine ~ machine.reset()
repl ~ from air_quality_monitor.monitor import main ~ main()
