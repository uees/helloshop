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

// config data
var confData map[string]interface{}

// BasePath 基础路径
var BasePath string

// DBConfig 数据库配置
var DBConfig dBConfig

// ServerConfig 服务端配置
var ServerConfig serverConfig

// APIConfig api 配置
var APIConfig apiConfig

// WeAppConfig wx 配置
var WeAppConfig weAppConfig

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

type weAppConfig struct {
	CodeToSessURL string
	AppID         string
	Secret        string
}

type apiConfig struct {
	Prefix string
	URL    string
}

func initBasePath() {
	if BasePath == "" {
		_, filename, _, _ := runtime.Caller(1)
		BasePath = path.Dir(path.Dir(filename))
	}
}

func initConfigData() {
	if confData != nil {
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

	if err := json.Unmarshal(bytes, &confData); err != nil {
		fmt.Println("invalid config: ", err.Error())
	}
}

func initDBConfig() {
	err := utils.FillStructByJSON(&DBConfig, confData["database"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
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

func initServerConfig() {
	err := utils.FillStructByJSON(&ServerConfig, confData["go"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}

func initWeAppConfig() {
	err := utils.FillStructByJSON(&WeAppConfig, confData["weApp"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}

func initAPIConfig() {
	err := utils.FillStructByJSON(&APIConfig, confData["api"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}

func init() {
	initBasePath()
	initConfigData()
	initDBConfig()
	initServerConfig()
	// initWeAppConfig()
	// initAPIConfig()
}
