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

// Instance 配置组件对象
var Instance Config

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

// Config 组件
type Config struct {
	data         map[string]interface{}
	BasePath     string
	DBConfig     dBConfig
	ServerConfig serverConfig
	APIConfig    apiConfig
	WeAppConfig  weAppConfig
}

// GetName method
func (Config) GetName() string {
	return "config"
}

// SetUp 初始化方法
func (c *Config) SetUp() {
	c.initBasePath()
	c.initConfigMap()
	c.initDBConfig()
	c.initServerConfig()
	// initWeAppConfig()
	// initAPIConfig()
}

func (c *Config) initBasePath() {
	if c.BasePath == "" {
		_, filename, _, _ := runtime.Caller(1)
		c.BasePath = path.Dir(path.Dir(filename))
	}
}

func (c *Config) initConfigMap() {
	bytes, err := ioutil.ReadFile(path.Join(c.BasePath, "configuration.json"))
	if err != nil {
		fmt.Println("ReadFile: ", err.Error())
	}

	// 删除 JSON 中的注释
	configStr := string(bytes[:])
	configStr = regexp.MustCompile(`/\*.*\*/`).ReplaceAllString(configStr, "")
	bytes = []byte(configStr)

	if err := json.Unmarshal(bytes, &c.data); err != nil {
		fmt.Println("invalid config: ", err.Error())
	}
}

func (c *Config) initDBConfig() {
	err := utils.FillStructByJSON(&c.DBConfig, c.data["database"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
	if c.DBConfig.Engine != "mysql" {
		panic(fmt.Errorf("不支持的数据库"))
	}

	portStr := strconv.Itoa(c.DBConfig.Port)

	// 设置 DBConfig.URL
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{database}", c.DBConfig.Name, -1)
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{user}", c.DBConfig.User, -1)
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{password}", c.DBConfig.Password, -1)
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{host}", c.DBConfig.Host, -1)
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{port}", portStr, -1)
	c.DBConfig.URL = strings.Replace(c.DBConfig.URL, "{charset}", c.DBConfig.Charset, -1)
}

func (c *Config) initServerConfig() {
	err := utils.FillStructByJSON(&c.ServerConfig, c.data["go"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}

func (c *Config) initWeAppConfig() {
	err := utils.FillStructByJSON(&c.WeAppConfig, c.data["weApp"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}

func (c *Config) initAPIConfig() {
	err := utils.FillStructByJSON(&c.APIConfig, c.data["api"].(map[string]interface{}))
	if err != nil {
		panic(err)
	}
}
