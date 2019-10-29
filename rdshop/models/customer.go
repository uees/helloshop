package models

// Customer customers 表
type Customer struct {
}

// TableName 设置表名
func (Customer) TableName() string {
	return "customers"
}
