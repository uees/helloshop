package components

import (
	"fmt"
	"log"
	"time"

	"github.com/robfig/cron"
)

// TimerRegister Timer 注册器
func TimerRegister() {
	c := cron.New()

	c.AddFunc("0 0/5 * * * *", task)

	c.Start()
	log.Println("timer is running...")
}

func task() {
	fmt.Printf("%s : testing...\n", time.Now().Format("2006-01-02 15:04:05"))
}
