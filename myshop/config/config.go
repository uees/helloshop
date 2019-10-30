package config

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"myshop/utils"
	"path"
	"regexp"
	"runtime"
	"strconv"
	"strings"
)

func init() {
	initBasePath()
	initConfigMap()
	initDBConfig()
	initServerConfig()
	// initWeAppConfig()
	// initAPIConfig()
}

// BasePath 目录
var BasePath string

func initBasePath() {
	if BasePath == "" {
		_, filename, _, _ := runtime.Caller(1)
		BasePath = path.Dir(path.Dir(filename))
	}
}

// 配置数据
var configMap map[string]interface{}

func initConfigMap() {
	// 保证只读取一次配置文件
	if configMap != nil {
		return
	}

	bytes, err := ioutil.ReadFile(path.Join(BasePath, "configuration.json"))
	if err != nil {
		fmt.Println("ReadFile: ", err.Error())
	}

	// 删除 JSON 中的注释
	configStr := string(bytes[:])
	configStr = regexp.MustCompile(`/\*.*\*/`).ReplaceAllString(configStr, "")
	bytes = []byte(configStr)

	if err := json.Unmarshal(bytes, &configMap); err != nil {
		fmt.Println("invalid config: ", err.Error())
	}
}

type dBConfig struct {
	Engine       string
	Name         string
	User         string
	Password     string
	Charset      string
	Host         string
	Port         int
	SQLLog       bool
	URL          string
	MaxIdleConns int
	MaxOpenConns int
}

// DBConfig 数据库相关配置
var DBConfig dBConfig

func initDBConfig() {
	utils.SetStructByJSON(&DBConfig, configMap["database"].(map[string]interface{}))
	if DBConfig.Engine != "mysql" {
		panic(fmt.Errorf("不支持的数据库"))
	}

	portStr := strconv.Itoa(DBConfig.Port)

	// 设置 DBConfig.URL
	DBConfig.URL = strings.Replace(DBConfig.URL, "{database}", DBConfig.Name, -1)
	DBConfig.URL = strings.Replace(DBConfig.URL, "{user}", DBConfig.User, -1)
	DBConfig.URL = strings.Replace(DBConfig.URL, "{password}", DBConfig.Password, -1)
	DBConfig.URL = strings.Replace(DBConfig.URL, "{host}", DBConfig.Host, -1)
	DBConfig.URL = strings.Replace(DBConfig.URL, "{port}", portStr, -1)
	DBConfig.URL = strings.Replace(DBConfig.URL, "{charset}", DBConfig.Charset, -1)
}

type serverConfig struct {
	Debug       bool
	Port        int
	ImgHost     string
	SessionID   string
	MaxOrder    int
	MinOrder    int
	PageSize    int
	MaxPageSize int
	MinPageSize int
}

// ServerConfig 服务器相关配置
var ServerConfig serverConfig

func initServerConfig() {
	utils.SetStructByJSON(&ServerConfig, configMap["go"].(map[string]interface{}))
}

type weAppConfig struct {
	CodeToSessURL string
	AppID         string
	Secret        string
}

// WeAppConfig 微信小程序相关配置
var WeAppConfig weAppConfig

func initWeAppConfig() {
	utils.SetStructByJSON(&WeAppConfig, configMap["weApp"].(map[string]interface{}))
}

type apiConfig struct {
	Prefix string
	URL    string
}

// APIConfig api相关配置
var APIConfig apiConfig

func initAPIConfig() {
	utils.SetStructByJSON(&APIConfig, configMap["api"].(map[string]interface{}))
}
