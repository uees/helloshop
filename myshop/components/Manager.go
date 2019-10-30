package components

// IComponent 组件接口
type IComponent interface {
	SetUp()
	GetName() string
}

// Manager 组件管理器
var Manager = &CManager{
	Registered: map[string]bool{},
}

// CManager 组件管理器结构体
type CManager struct {
	Registered map[string]bool
	Components []*IComponent
}

// Register 注册组件
func (m *CManager) Register(components ...IComponent) {
	for _, component := range components {
		componentName := component.GetName()
		if !m.Registered[componentName] {
			m.Registered[componentName] = true
			m.Components = append(m.Components, &component)
		}
	}
}

// Init 初始化注册的组件
func (m *CManager) Init() {
	for _, component := range m.Components {
		(*component).SetUp()
	}
}
