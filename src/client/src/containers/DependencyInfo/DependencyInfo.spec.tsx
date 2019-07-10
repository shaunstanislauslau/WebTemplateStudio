import * as React from "react";
import { shallow } from "enzyme";
import { WIZARD_CONTENT_INTERNAL_NAMES } from "../../utils/constants";
import DependencyInfo, { dependencies } from "./index";

describe("DependencyInfo", () => {
  let props: any;
  let wrapper: any;

  beforeEach(() => {
    props = {
      frameworkName: WIZARD_CONTENT_INTERNAL_NAMES.FLASK,
      intl: global.intl
    };
    wrapper = shallow(<DependencyInfo {...props} />);
  });

  it("renders without crashing", () => {
    expect(wrapper).toBeDefined();
  });
});
