package config

import (
	"testing"
)

func TestInitJSON(t *testing.T) {
	if configMap["webPoweredBy"] != "rdshop" {
		t.Errorf("webPoweredBy != rdshop")
	}
}

func TestDbConfig(t *testing.T) {
	if DBConfig.URL == "" {
		t.Errorf("no init DBConfig.URL")
	}
}
