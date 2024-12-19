module Jekyll
  class AutoPagesGenerator < Generator
    safe true

    def generate(site)
      dir = 'pages'
      layout = site.config['auto_pages']['layout'] || 'auto_page'
      files = Dir.glob("#{dir}/**/*").select { |f| File.file?(f) }

      files.each do |file|
        site.pages << AutoPage.new(site, site.source, file, layout)
      end
    end
  end

  class AutoPage < Page
    def initialize(site, base, file, layout)
      @site = site
      @base = base
      @dir = File.dirname(file)
      @name = File.basename(file)

      self.process(@name)
      self.read_yaml(@base, file)
      self.data['layout'] = layout
    end
  end
end
