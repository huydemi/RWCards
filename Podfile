source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '10.0'
use_frameworks!

target 'RWCards' do
  #  pod 'SwiftProtobuf', git: 'https://github.com/apple/swift-protobuf.git', :tag => '0.9.24'
  pod 'SwiftProtobuf'
pod 'Alamofire', '~> 4.0'
end

post_install do |installer|
    installer.pods_project.targets.each do |target|
        target.build_configurations.each do |config|
            config.build_settings['SWIFT_VERSION'] = '3.0'
        end
    end
  end
