package models

import "github.com/jinzhu/gorm"

// Post 帖子
type Post struct {
	gorm.Model
	Type            string `gorm:"type:varchar(32)" json:"type"`
	Title           string `json:"title"`
	Slug            string `json:"slug"`
	MetaDescription string `json:"meta_description"`
	MetaKeywords    string `json:"meta_keywords"`
	Content         string `gorm:"not null" json:"content"`
	Status          int    `json:"status"`
	CreatedUser     User   `gorm:"foreignkey:CreatedUserID"` // 使用 CreatedUserID 作为外键
	CreatedUserID   uint   `json:"created_user_id"`
	UpdatedUserID   uint   `json:"updated_user_id"`
}

// TableName 设置表名
func (Post) TableName() string {
	return "cms_post"
}
