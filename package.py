from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    def _init(self, **kwargs):
        if "branch" in kwargs.keys():
            self.branch = kwargs["branch"]
        else:
            self.branch = "master"

    def prepare(self):
        """
        is called at install time
        :return:
        """
        server = self.openresty
        server.install(reset=True)
        server.configure()
        website = server.websites.get("www_enertia_io")
        website.ssl = True
        website.port = 443
        locations = website.locations.get("main")
        static_location = locations.locations_static.new()
        static_location.name = "static"
        static_location.path_url = "/"
        static_location.path_location = f"/sanbox/code/github/Pishoy/www_enertia_io"
        static_location.use_jumpscale_weblibs = True
        website.domain = 'www.enertia.io'
        website.path = '/sanbox/code/github/Pishoy/www_enertia_io'
        locations.configure()
        website.configure()


    def start(self):
        """
        called when the 3bot starts
        :return:
        """
        self.prepare()

    def stop(self):
        """
        called when the 3bot stops
        :return:
        """
        pass

    def uninstall(self):
        """
        called when the package is no longer needed and will be removed from the threebot
        :return:
        """
        pass


