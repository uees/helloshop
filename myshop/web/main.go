package main

import (
	"fmt"
	"myshop/components"
	"myshop/config"
)

func init() {
	components.Manager.Register(&config.Instance)
	components.Manager.Init()
}

func main() {
	fmt.Println(config.Instance.DBConfig.URL)
}
