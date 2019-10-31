package components

import "myshop/utils"

// Register 组件接口
type Register func()

// Manager 组件管理器结构体
type Manager struct {
	Registered map[string]bool
	Registeres []Register
}

// NewManager Manager 工厂
func NewManager() *Manager {
	return &Manager{
		Registered: map[string]bool{},
	}
}

// Register 注册组件
func (m *Manager) Register(registeres ...Register) {
	for _, register := range registeres {
		name := utils.GetFunctionName(register)
		if !m.Registered[name] {
			m.Registered[name] = true
			m.Registeres = append(m.Registeres, register)
		}
	}
}

// Init 初始化注册的组件
func (m Manager) Init() {
	for _, register := range m.Registeres {
		register()
	}
}
