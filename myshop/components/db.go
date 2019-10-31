package components

import (
	"myshop/config"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

// DB *gorm.DB
var DB *gorm.DB

// DbRegister db 组件注册器
func DbRegister() {
	var err error
	DB, err = gorm.Open(config.DBConfig.Engine, config.DBConfig.URL)
	if err != nil {
		panic(err)
	}

	if config.DBConfig.SQLLog {
		DB.LogMode(true)
	}

	DB.DB().SetMaxIdleConns(config.DBConfig.MaxIdleConns)
	DB.DB().SetMaxOpenConns(config.DBConfig.MaxOpenConns)
}
