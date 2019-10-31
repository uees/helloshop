package models

import "time"

// User 表
type User struct {
	ID          uint      `gorm:"primary_key" json:"id"`
	Username    string    `json:"username"`
	FirstName   string    `json:"first_name"`
	LastName    string    `json:"last_name"`
	Email       string    `json:"email"`
	IsStaff     bool      `json:"is_staff"`
	IsActive    bool      `json:"is_active"`
	IsSuperuser bool      `json:"is_superuser"`
	LastLogin   time.Time `json:"last_login"`
	DateJoined  time.Time `json:"date_joined"`
}

// TableName 设置表名
func (User) TableName() string {
	return "auth_user"
}
