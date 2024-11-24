from apscheduler.schedulers.blocking import BlockingScheduler

from reserve import order
from sign import signing

# 创建调度器实例
scheduler = BlockingScheduler()

# 添加任务到调度器，使用cron表达式设置执行时间
# cron表达式格式为：(年, 月, 日, 时, 分, 秒) ，其中年和秒是可选的
# 在这里，我们设置每天（不指定日期，使用*）的6点15分（6, 15）执行任务
scheduler.add_job(order, 'cron', hour=6, minute=15)
scheduler.add_job(order, 'cron', hour=6, minute=16)
scheduler.add_job(order, 'cron', hour=6, minute=17)
scheduler.add_job(order, 'cron', hour=6, minute=18)
scheduler.add_job(signing, 'cron', hour=12, minute=1)
scheduler.add_job(signing, 'cron', hour=12, minute=2)
scheduler.add_job(signing, 'cron', hour=12, minute=3)
scheduler.add_job(signing, 'cron', hour=16, minute=16)
scheduler.add_job(signing, 'cron', hour=16, minute=17)
scheduler.add_job(signing, 'cron', hour=16, minute=18)

try:
    # 启动调度器
    print("调度器开始")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    # 当用户中断程序（如Ctrl+C）时，优雅地退出
    print("调度器已停止")
