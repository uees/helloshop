package utils

import (
	"errors"
	"fmt"
	"reflect"
	"runtime"

	"golang.org/x/crypto/bcrypt"
)

var monthMap = map[string]int{
	"January":   0,
	"February":  1,
	"March":     2,
	"April":     3,
	"May":       4,
	"June":      5,
	"July":      6,
	"August":    7,
	"September": 8,
	"October":   9,
	"November":  10,
	"December":  11,
}

// 设置 obj 对象上指定 name 字段的值 value
func setField(obj interface{}, name string, value interface{}) error {
	structData := reflect.ValueOf(obj).Elem()
	fieldValue := structData.FieldByName(name)

	if !fieldValue.IsValid() {
		return fmt.Errorf("No such field: %s in obj ", name)
	}

	if !fieldValue.CanSet() {
		return fmt.Errorf("Cannot set %s field value ", name)
	}

	fieldType := fieldValue.Type()
	val := reflect.ValueOf(value)

	valTypeStr := val.Type().String()
	fieldTypeStr := fieldType.String()
	if valTypeStr == "float64" && fieldTypeStr == "int" {
		val = val.Convert(fieldType)
	} else if fieldType != val.Type() {
		return errors.New("Provided value type " + valTypeStr + " didn't match obj field type " + fieldTypeStr)
	}
	fieldValue.Set(val)
	return nil
}

// FillStructByJSON 由 json 对象生成 struct
func FillStructByJSON(obj interface{}, mapData map[string]interface{}) error {
	for key, value := range mapData {
		if err := setField(obj, key, value); err != nil {
			fmt.Println(err.Error())
			return err
		}
	}
	return nil
}

// MonthIndex 字符串月份转整数月份
func MonthIndex(month string) int {
	return monthMap[month]
}

// PasswordHash 将密码加密
func PasswordHash(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
	return string(bytes), err
}

// PasswordVerify 验证密码
func PasswordVerify(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
}

// GetFunctionName 获取函数的名称
func GetFunctionName(i interface{}) string {
	return runtime.FuncForPC(reflect.ValueOf(i).Pointer()).Name()
}
