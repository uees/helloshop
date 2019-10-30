package config

import (
	"testing"
)

func TestConfig(t *testing.T) {
	Instance.SetUp()
	if Instance.DBConfig.URL == "{user}:{password}@tcp({host}:{port})/{database}?charset={charset}&parseTime=True&loc=Local" {
		t.Errorf("init fail")
	}
}
