Recess filter for webassets
===========================

Install::

    pip install webassets-recess

Register::

    from webassets.filter import register_filter
    from webassets_recess import RecessFilter
        
    register_filter(RecessFilter)

Example usage::

  from webassets.loaders import YAMLLoader
  for name, bundle in YAMLLoader('webassets.yaml').load_bundles().items():
      assets.register(name, bundle)

Where webassets.yaml contains::

    css_all:
    filters: recess,cssutils
    output: cache/default.css
    contents:
        - bootstrap/less/bootstrap.less

Now you can hack bootsrap less. Merges are on you.
