from dataclasses import dataclass


@dataclass(frozen=True)
class SideMenuItems:
    Overview = 'sidebar-item-overview'
    GatewayServices = 'sidebar-item-gateway-services'
    Routes = 'sidebar-item-routes'
    Consumers = 'sidebar-item-consumers'
    Plugins = 'sidebar-item-plugins'
    RedisConfigurations = 'sidebar-item-redis-configurations'
    Upstreams = 'sidebar-item-upstreams'
    Certificate = 'sidebar-item-certificates'
    SNIs = 'sidebar-item-snis'
    Keys = 'sidebar-item-keys'
    Vaults = 'sidebar-item-vaults'

@dataclass(frozen=True)
class ServicesPageItems:
    AddGatewayServiceEmpty = 'empty-state-action'
    AddGatewayService = 'toolbar-add-gateway-service'
    FilterButton = 'filter-button'

@dataclass(frozen=True)
class ServicesFormPageItems :
  GatewayServiceNameInput = 'gateway-service-name-input'
  GatewayServiceTagsInput = 'gateway-service-tags-input'
  GatewayServiceURLRadioBtn = 'gateway-service-url-radio'
  GatewayServiceFullURLInput = 'gateway-service-url-input'
  GatewayServiceProtocolRadioBtn = 'gateway-service-protocol-radio'
  AdvancedFieldsExpandBtn = 'collapse-trigger-content'
  GatewayServiceRetriesInput = 'gateway-service-retries-input'
  GatewayServiceFormSubmit = 'service-create-form-submit'
  GatewayServiceFormCancel = 'service-create-form-cancel'
  FormError = 'form-error'

@dataclass(frozen=True)
class ServiceItemDetailsPageItems:
  Configuration = 'show-service'
  Routes = 'service-routes'
  Plugins = 'service-plugins'
  Document = 'service-documents'
  ServiceID = 'id-copy-uuid'
  ServiceName = 'name-property-value'
  AddRoutesBtnEmpty = 'empty-state-action'
  AddRouteBtn = 'toolbar-add-route'

@dataclass(frozen=True)
class RoutesFormPageItems:
  GatewayRoutesNameInput = 'route-form-name'
  RoutesServiceInput = 'route-form-service-id'
  RoutesTagsInput = 'route-form-tags'
  RoutesProtocolsDropdown = 'route-form-protocols'
  RoutesPathInput = 'route-form-paths-input-1'
  AdvancedFieldsExpandBtn = 'collapse-trigger-content'
  RoutesPathHandlingDropdown = 'route-form-path-handling'
  RoutesFormSubmit = 'route-create-form-submit'
  RoutesFormCancel = 'route-create-form-cancel'
  FormError = 'form-error'