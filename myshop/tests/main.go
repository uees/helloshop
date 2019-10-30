package main

import (
	"fmt"
	"os"

	"github.com/jinzhu/gorm"
)

func main() {
	db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(-1)
	}

	defer db.Close()
}
