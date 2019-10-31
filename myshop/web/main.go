package main

import (
	"fmt"
	"myshop/components"
	"myshop/models"
)

func init() {
	manager := components.NewManager()
	manager.Register(components.DbRegister)
	manager.Init()
}

func main() {
	var user models.User
	components.DB.First(&user, 1) // 查询 id 为 1 的 product
	fmt.Println(user.Username, user.Email)
}
