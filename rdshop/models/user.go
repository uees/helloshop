package models

import "time"

// User 表
type User struct {
	ID         uint      `gorm:"primary_key" json:"id"`
	Username   string    `json:"username"`
	FirstName  string    `json:"first_name"`
	LastName   string    `json:"last_name"`
	Email      string    `json:"email"`
	IsStaff    bool      `json:"is_staff"`
	IsActive   bool      `json:"is_active"`
	DateJoined time.Time `json:"date_joined"`
}

// TableName 通过此方法将 Post 表命名为`profiles`
func (User) TableName() string {
	return "auth_user"
}
