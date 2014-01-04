require 'yaml'

class Settings
    @@file_name = "#{File.dirname(__FILE__)}/settings.conf"
    @@content = nil

    def self.content
        unless @@content
            if File.exists? @@file_name
                @@content = YAML.load File.read @@file_name
            else
                # Default values
                @@content = {
                    :colors => [0xff0000, 0x00ff00, 0x0000ff, 0xffff00,
                                0x00ffff, 0xff00ff, 0xc0c0c0, 0x600000,
                                0x009900, 0x339999, 0xcc6633, 0xff3300],
                }
            end
        end
        return @@content
    end

    def self.dump
        File.write @@file_name, @@content.to_yaml
    end

    def self.[] key
        return content[key]
    end

    def self.[]= key, value
        content[key] = value
    end
end
